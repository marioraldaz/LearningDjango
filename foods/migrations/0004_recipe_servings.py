# Generated by Django 5.0.3 on 2024-04-29 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foods", "0003_alter_ingredient_spoonacular_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="servings",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
    ]