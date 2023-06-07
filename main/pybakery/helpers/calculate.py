from pybakery.models import Basket, Calculation
from pint import UnitRegistry

ureg = UnitRegistry()

def calculate():
    basket = Basket.objects.all()
    basket = sumIngredients(basket)
    basket = [Calculation(ingredient = ingredient, 
                          quantity = quant_unit.m, 
                          unit = quant_unit.units) 
              for ingredient, quant_unit in basket.items()]
    Calculation.objects.bulk_create(basket)

def sumIngredients(ingredients:list) -> dict:
    agg_sum = {}
    for ingredient in ingredients:
        unit = ingredient.unit
        quant = ingredient.default_quantity
        ingredient = ingredient.ingredient
        # need better way of identifing if unit of measure is the ingredient
        if unit not in ureg:
            ureg.define(f'{unit} = [{unit}]')
        agg_sum[ingredient] = _baking_sum(agg_sum.get(ingredient, 0 * ureg(unit)),
                                          (quant * ureg(unit)))
    return agg_sum

def _baking_sum(pint_object1, pint_object2):
    # breakpoint()
    unit = max(pint_object1.units, pint_object2.units)
    bsum = (pint_object1 + pint_object2).to(unit)
    return bsum
