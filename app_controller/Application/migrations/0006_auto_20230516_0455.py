# Generated by Django 3.2.9 on 2023-05-15 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0005_alter_product_type_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=None, help_text='Category 3 မျိုးထည်း မှ ရွေးချယ်ပေးပါ။', on_delete=django.db.models.deletion.CASCADE, to='Application.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(default=None, help_text='အမျိုးအစားများ အကန့်အသတ် မရှိထက်ထည့်နိုင်သည်။', on_delete=django.db.models.deletion.CASCADE, to='Application.product_type'),
        ),
    ]
