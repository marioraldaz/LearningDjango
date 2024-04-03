# Generated by Django 5.0.2 on 2024-04-03 12:15

import django.core.validators
import django.db.models.deletion
import profiles.utils.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDaily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('total_calories_consumed', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0), profiles.utils.validators.validate_positive_float])),
                ('total_protein_consumed', models.FloatField(default=0.0)),
                ('total_fat_consumed', models.FloatField(default=0.0)),
                ('total_carbohydrates_consumed', models.FloatField(default=0.0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
            ],
        ),
    ]
