# Generated by Django 3.1.2 on 2021-05-16 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderApp', '0003_auto_20210516_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Цена заказа'),
        ),
    ]
