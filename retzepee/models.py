from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Prefetch


class RecipeQuerySet(models.QuerySet):
    def prefetch_ingredients(self):
        return self.prefetch_related(
            Prefetch(
                'ingredientforrecipe_set',
                queryset=IngredientForRecipe.objects.select_related('ingredient', 'ingredient_measurement')
            )
        )


class Recipe(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField()

    ingredients = models.ManyToManyField('retzepee.Ingredient', through='retzepee.IngredientForRecipe')
    instructions = models.TextField()

    yields_portions = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1)])

    objects = RecipeQuerySet.as_manager()

    def __str__(self):
        return self.title


class Measurement(models.Model):
    name = models.CharField(max_length=50)
    token = models.CharField(max_length=10)

    class Meta:
        unique_together = [['name', 'token']]

    def __str__(self):
        return f'{self.name} ({self.token})'


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class IngredientForRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ingredient_amount = models.DecimalField(
        max_digits=10, decimal_places=3, null=True, blank=True, validators=[MinValueValidator(0)]
    )
    ingredient_measurement = models.ForeignKey(Measurement, null=True, blank=True, on_delete=models.CASCADE)

    position = models.SmallIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        unique_together = [['recipe', 'position']]
