# Generated by Django 3.2.9 on 2023-05-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0006_auto_20230516_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
