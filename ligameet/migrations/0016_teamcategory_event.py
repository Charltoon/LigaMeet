# Generated by Django 5.1.2 on 2024-11-05 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligameet', '0015_remove_event_number_of_teams_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamcategory',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_categories', to='ligameet.event'),
        ),
    ]
