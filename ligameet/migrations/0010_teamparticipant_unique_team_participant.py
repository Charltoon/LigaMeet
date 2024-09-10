# Generated by Django 5.0.7 on 2024-09-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligameet', '0009_teamevent_teamevent_unique_team_event'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='teamparticipant',
            constraint=models.UniqueConstraint(fields=('PART_ID', 'TEAM_ID'), name='unique_team_participant'),
        ),
    ]