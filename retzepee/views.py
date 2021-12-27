from django.views.generic import DetailView

from retzepee.models import Recipe


class RecipeView(DetailView):
    model = Recipe
    template_name = 'retzepee/recipe.html'

    def get_queryset(self):
        return super().get_queryset().prefetch_ingredients()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.object.title

        return ctx
