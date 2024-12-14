# Generated by Django 5.1.2 on 2024-12-11 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligameet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BracketData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teams', models.JSONField()),
                ('results', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sport_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brackets', to='ligameet.sportdetails')),
            ],
        ),
    ]
