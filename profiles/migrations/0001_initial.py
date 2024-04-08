# Generated by Django 5.0.2 on 2024-04-03 12:14

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models
from ...food_intake.user_daily import UserDaily


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('calories', models.FloatField()),
                ('protein', models.FloatField()),
                ('fat', models.FloatField()),
                ('carbohydrates', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodIntake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_type', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack')], default='Breakfast', max_length=20, verbose_name='Meal Type')),
                ('intake_date', models.DateField(default=django.utils.timezone.now, verbose_name='Intake Date')),
            ],
            options={
                'db_table': 'profiles_foodintake',
            },
        ),
        migrations.CreateModel(
            name='SavedRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.IntegerField(default=1, unique=True)),
                ('profile_id', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, unique=True, validators=[django.core.validators.MinLengthValidator(6)])),
                ('password', models.CharField(max_length=85, validators=[django.core.validators.MinLengthValidator(6)])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('weight', models.IntegerField(default=80)),
                ('height', models.IntegerField(default=170)),
                ('date_of_birth', models.DateField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('activityLevel', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FoodIntakeDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=255)),
                ('item_type', models.CharField(max_length=20)),
                ('food_intake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='profiles.foodintake')),
            ],
        ),
        migrations.AddField(
            model_name='foodintake',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile'),
        ),
        migrations.CreateModel(
            name='UserRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
            ],
        ),
    ]
