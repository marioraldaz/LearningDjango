# Generated by Django 5.0.2 on 2024-03-13 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_rename_user_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='activityLevel',
            field=models.IntegerField(choices=[('Sedentary', 'Sedentary'), ('slightly_active', 'slightly_active'), ('moderately_active', 'moderately_active'), ('very_active', 'very_active'), ('super_active', 'super_active')], default=''),
        ),
    ]