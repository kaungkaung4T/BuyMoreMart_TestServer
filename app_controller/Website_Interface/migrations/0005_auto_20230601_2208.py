# Generated by Django 3.2.9 on 2023-06-01 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website_Interface', '0004_header_imagegroup_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='header_imagegroup',
            name='name',
            field=models.CharField(blank=True, default='Edit', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='index_imagegroup',
            name='name',
            field=models.CharField(blank=True, default='Edit', max_length=255, null=True),
        ),
    ]
