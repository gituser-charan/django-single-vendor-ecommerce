# Generated by Django 3.2.12 on 2024-02-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0006_auto_20240213_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.CharField(max_length=36, verbose_name='Payment ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='provider_order_id',
            field=models.CharField(max_length=40, verbose_name='Order ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='signature_id',
            field=models.CharField(max_length=128, verbose_name='Signature ID'),
        ),
    ]