from django.contrib import admin
from .models import Recipe, Ingredient

# Register your models here.
class IngredientInline(admin.TabularInline):
    model = Ingredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]
