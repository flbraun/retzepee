# Generated by Django 4.0 on 2021-12-12 21:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientForRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_amount', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('position', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retzepee.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField()),
                ('instructions', models.TextField()),
                ('yields_portions', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('ingredients', models.ManyToManyField(through='retzepee.IngredientForRecipe', to='retzepee.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('token', models.CharField(max_length=10)),
            ],
            options={
                'unique_together': {('name', 'token')},
            },
        ),
        migrations.AddField(
            model_name='ingredientforrecipe',
            name='ingredient_measurement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='retzepee.measurement'),
        ),
        migrations.AddField(
            model_name='ingredientforrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retzepee.recipe'),
        ),
        migrations.AlterUniqueTogether(
            name='ingredientforrecipe',
            unique_together={('recipe', 'position')},
        ),
    ]
