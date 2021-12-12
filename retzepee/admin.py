from django.contrib import admin

from retzepee.models import Recipe, Measurement, Ingredient, IngredientForRecipe


class IngredientForRecipeInline(admin.TabularInline):
    model = IngredientForRecipe
    fields = ('position', 'ingredient_amount', 'ingredient_measurement', 'ingredient')
    autocomplete_fields = ('ingredient', 'ingredient_measurement')
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [IngredientForRecipeInline]


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    search_fields = ('name', 'token')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('name',)
