# Generated by Django 4.2.3 on 2023-09-28 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0013_cancelorder_is_cancelled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_cancelled',
        ),
    ]