from django.db import models
from pint import UnitRegistry
ureg = UnitRegistry()


# main application models
class Recipe(models.Model):
    name = models.fields.CharField(max_length=500, unique=True)
    image = models.ImageField(upload_to='images/',
                              height_field='image_height',
                              width_field='image_width',)
    
    image_height = models.PositiveIntegerField(default=250)
    image_width = models.PositiveIntegerField(default=250)

    quantity = models.fields.IntegerField()

    def __str__(self):
        return f'{self.name}'

    def addToBasket(self, quant):
        ingredients = self.ingredients.all()
        for ingredient in ingredients:
            if ingredient.unit in ureg:
                reduced_quantity = ingredient.default_quantity * ureg(ingredient.unit)
                reduced_quantity = reduced_quantity.to_base_units()
                base_unit = reduced_quantity.units
                reduced_quantity = reduced_quantity.m
            else:
                reduced_quantity = ingredient.default_quantity
                base_unit = ingredient.unit

            recipe_quantity = quant / ingredient.recipe.quantity

            Basket.objects.create(
                recipe = ingredient.recipe_id,
                ingredient = ingredient.ingredient,
                unit = ingredient.unit,
                default_quantity = ingredient.default_quantity * recipe_quantity,
                recipe_quantity = recipe_quantity,
                base_quantity = reduced_quantity * recipe_quantity,
                base_unit = base_unit
            )


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, to_field='name',
                               related_name='ingredients',
                               on_delete=models.CASCADE)
    
    ingredient = models.CharField(max_length=250)
    unit = models.CharField(max_length=250)
    default_quantity = models.FloatField()

    class Meta:
        unique_together = ('recipe', 'ingredient')

    def __str__(self):
        return f'{self.ingredient} ({self.recipe})'


# class pintField(models.Field):
#     description = "a quantity-unit pair"

#     def __init__(self, *args, **kwargs):
#         kwargs['max_length'] = 11
#         kwargs['blank'] = False
#         kwargs['null'] = False
#         super().__init__(*args, **kwargs)

#     def deconstruct(self):
#         name, path, args, kwargs = super().deconstruct()
#         del kwargs['max_length'], kwargs['blank'], kwargs['null']
#         return name, path, args, kwargs

#     def db_type(self, connection: Any) -> str:
#         return super().db_type(connection)


class Basket(models.Model):
    recipe = models.fields.TextField()
    ingredient = models.fields.TextField()
    unit = models.fields.TextField()
    default_quantity = models.fields.FloatField()
    recipe_quantity = models.fields.FloatField()
    base_unit = models.fields.TextField()
    base_quantity = models.fields.FloatField()
    
    def __str__(self):
        return f'{self.ingredient} ({self.recipe})'


class Calculation(models.Model):
    ingredient = models.fields.TextField()
    quantity = models.fields.DecimalField(max_digits=10, decimal_places=3)
    unit = models.fields.TextField()

    def __str__(self):
        return f'{self.ingredient}'