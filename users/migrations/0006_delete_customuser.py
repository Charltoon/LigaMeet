# Generated by Django 5.0.7 on 2024-08-24 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]