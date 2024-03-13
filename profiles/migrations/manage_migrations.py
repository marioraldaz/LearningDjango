from django.db import migrations

def handle_empty_activity_level(apps, schema_editor):
    UserProfile = apps.get_model('profiles', 'UserProfile')
    for profile in UserProfile.objects.filter(activityLevel=''):
        profile.activityLevel = 'Sedentary'  # Set a default value or choose appropriate handling
        profile.save()

class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0006_userprofile_activitylevel'),  # Adjust the dependency to match the correct migration
    ]

    operations = [
        migrations.RunPython(handle_empty_activity_level),
    ]
