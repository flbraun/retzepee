from django.db.models import Prefetch
from django.views.generic import DetailView

from retzepee.models import IngredientForRecipe, Recipe


class RecipeView(DetailView):
    model = Recipe
    template_name = 'retzepee/recipe.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.prefetch_related(
            Prefetch(
                'ingredientforrecipe_set',
                queryset=IngredientForRecipe.objects.select_related('ingredient', 'ingredient_measurement')
            )
        )
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.object.title

        return ctx
