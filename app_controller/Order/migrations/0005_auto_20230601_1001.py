# Generated by Django 3.2.9 on 2023-06-01 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_auto_20230523_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='each_product',
            field=models.TextField(help_text='နံပါတ်များသည် မှာယူထားသော ပစ္စည်း အရေအတွက် ဖြစ်သည်။'),
        ),
        migrations.AlterField(
            model_name='order',
            name='grand_total_price',
            field=models.IntegerField(help_text='ပစ္စည်းအားလုံး နှင့် Delivery fee စုစုပေါင်းကျသင့်ငွေ။'),
        ),
    ]