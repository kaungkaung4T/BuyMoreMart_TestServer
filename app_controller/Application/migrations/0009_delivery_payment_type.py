# Generated by Django 3.2.9 on 2023-05-21 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0008_alter_cart_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('iamge', models.ImageField(blank=True, null=True, upload_to='payment_image')),
            ],
        ),
    ]
