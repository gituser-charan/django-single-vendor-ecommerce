# Generated by Django 3.2.12 on 2024-04-24 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0016_auto_20240424_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='allow_distance',
            new_name='allow_radius',
        ),
        migrations.RemoveField(
            model_name='store',
            name='search_radius',
        ),
    ]
