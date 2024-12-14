# Generated by Django 5.1.2 on 2024-12-13 17:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ligameet', '0006_rename_vb_stats_assist_volleyballstats_assists_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='playerstats',
            unique_together={('player', 'match', 'sport')},
        ),
    ]
