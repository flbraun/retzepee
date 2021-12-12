from django.core.management import BaseCommand

from retzepee.models import Measurement, Ingredient, Recipe

DEFAULT_MEASUREMENTS = [
    ('Teelöffel', 'TL'),
    ('Esslöffel', 'EL'),
    ('Teelöffel', 'tsp'),
    ('Esslöffel', 'tbsp'),
    ('Gramm', 'g'),
    ('Kilogramm', 'kg'),
    ('Milliliter', 'ml'),
    ('Liter', 'l'),
]

DEFAULT_INGREDIENTS = [
    'Tomaten',
    'Wasser',
    'Gemüsebrühe',
    'Salz',
    'Pfeffer',
    'Hackfleisch',
    'Kidneybohnen',
    'Mais',
    'Chiliflocken',
    'Honig',
    'Dijon-Senf',
    'Aceto Balsamico',
    'Olivenöl',
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for m in DEFAULT_MEASUREMENTS:
            Measurement.objects.get_or_create(name=m[0], token=m[1])

        for i in DEFAULT_INGREDIENTS:
            Ingredient.objects.get_or_create(name=i)

        chili_con_carne, _ = Recipe.objects.get_or_create(
            title='Chili Con Carne',
            defaults=dict(
                slug='chili-con-carne',
                yields_portions=5,
                instructions='Alles mischen. Alles kochen.',
            ),
        )
        chili_con_carne.ingredients.add(
            Ingredient.objects.get(name='Hackfleisch'),
            through_defaults=dict(
                position=1,
                ingredient_amount=800,
                ingredient_measurement=Measurement.objects.get(token='g'),
            ),
        )
        chili_con_carne.ingredients.add(
            Ingredient.objects.get(name='Kidneybohnen'),
            through_defaults=dict(
                position=2,
                ingredient_amount=800,
                ingredient_measurement=Measurement.objects.get(token='g'),
            ),
        )
        chili_con_carne.ingredients.add(
            Ingredient.objects.get(name='Mais'),
            through_defaults=dict(
                position=3,
                ingredient_amount=200,
                ingredient_measurement=Measurement.objects.get(token='g'),
            ),
        )
        chili_con_carne.ingredients.add(
            Ingredient.objects.get(name='Salz'),
            through_defaults=dict(
                position=4,
                ingredient_amount=1,
                ingredient_measurement=Measurement.objects.get(token='TL'),
            ),
        )
        chili_con_carne.ingredients.add(
            Ingredient.objects.get(name='Chiliflocken'),
            through_defaults=dict(
                position=5,
                ingredient_amount=1,
                ingredient_measurement=Measurement.objects.get(token='TL'),
            ),
        )

        vinaigrette, _ = Recipe.objects.get_or_create(
            title='Balsamico-Vinaigrette',
            defaults=dict(
                slug='balsamico-vinaigrette',
                instructions=(
                    'Alle Zutaten in ein verschließbares Gefäß geben. Schütteln, bis sich ein eine '
                    'homogene Emulsion ergeben hat.\nDie Menge reicht ungefähr für einen mittelgroßen Salatkopf.'
                ),
            ),
        )
        vinaigrette.ingredients.add(
            Ingredient.objects.get(name='Aceto Balsamico'),
            through_defaults=dict(
                position=1,
                ingredient_amount=1,
                ingredient_measurement=Measurement.objects.get(token='tbsp'),
            ),
        )
        vinaigrette.ingredients.add(
            Ingredient.objects.get(name='Olivenöl'),
            through_defaults=dict(
                position=2,
                ingredient_amount=3,
                ingredient_measurement=Measurement.objects.get(token='tbsp'),
            ),
        )
        vinaigrette.ingredients.add(
            Ingredient.objects.get(name='Honig'),
            through_defaults=dict(
                position=3,
                ingredient_amount=2,
                ingredient_measurement=Measurement.objects.get(token='tsp'),
            ),
        )
        vinaigrette.ingredients.add(
            Ingredient.objects.get(name='Dijon-Senf'),
            through_defaults=dict(
                position=4,
                ingredient_amount=1,
                ingredient_measurement=Measurement.objects.get(token='tsp'),
            ),
        )
        vinaigrette.ingredients.add(
            Ingredient.objects.get(name='Salz'),
            through_defaults=dict(
                position=5,
            ),
        )
        vinaigrette.ingredients.add(
            Ingredient.objects.get(name='Pfeffer'),
            through_defaults=dict(
                position=6,
            ),
        )
