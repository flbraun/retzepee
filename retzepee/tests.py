from django.test import Client
from django.urls import reverse

from retzepee.models import Recipe
from retzepee.utils import RetzepeeTestCase
from retzepee.views import RecipeView


class RecipeViewTestCase(RetzepeeTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.recipe = Recipe.objects.create(
            title='Sample Recipe',
            slug='sample-recipe',
            instructions='Cook. Eat. Feel good.',
            yields_portions=5,
        )

    def test_url_matching(self):
        self.assertURLResolvesToView('/recipe/42/', RecipeView)
        self.assertURLResolvesToView('/recipe/42/', RecipeView)
        self.assertURLResolvesToView('/recipe/42/some-slug/', RecipeView)

    def test_url_reversing(self):
        self.assertEqual(reverse('recipe-detail', kwargs={'pk': self.recipe.pk}), f'/recipe/{self.recipe.pk}/')
        self.assertEqual(
            reverse('recipe-detail-with-slug', kwargs={'pk': self.recipe.pk, 'slug': self.recipe.slug}),
            f'/recipe/{self.recipe.pk}/{self.recipe.slug}/',
        )

    def test_get(self):
        client = Client(f'/recipe/{self.recipe.pk}/')

        with self.assertNumQueries(2):
            res = client.get(f'/recipe/{self.recipe.pk}/')
        self.assertEqual(res.status_code, 200)
