# Generated by Django 5.0.1 on 2024-10-10 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligameet', '0004_event_event_image_alter_event_event_status'),
        ('users', '0003_profile_availability_profile_basketball_achievements_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sports',
            field=models.ManyToManyField(blank=True, to='ligameet.sport'),
        ),
    ]