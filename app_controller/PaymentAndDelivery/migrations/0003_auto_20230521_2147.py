# Generated by Django 3.2.9 on 2023-05-21 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaymentAndDelivery', '0002_rename_delivery_delivery_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_fee',
            name='city',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='delivery_fee',
            name='free',
            field=models.BooleanField(default=False),
        ),
    ]
