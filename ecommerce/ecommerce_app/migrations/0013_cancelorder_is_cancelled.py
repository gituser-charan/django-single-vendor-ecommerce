# Generated by Django 4.2.3 on 2023-09-28 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0012_cancelorder_order_is_cancelled'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancelorder',
            name='is_cancelled',
            field=models.BooleanField(default=True),
        ),
    ]
