# Generated by Django 3.1.2 on 2021-05-14 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_address', models.CharField(max_length=100, verbose_name='Адрес отправки')),
                ('delivery_address', models.CharField(max_length=100, verbose_name='Адрес доствки')),
                ('cargo_name', models.CharField(max_length=100, verbose_name='Описание груза')),
                ('cargo_weight', models.IntegerField(verbose_name='Вес груза')),
                ('cargo_volume', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Объем груза')),
                ('cargo_loading_date', models.DateField(verbose_name='Дата загрузки груза')),
                ('cargo_loading_time', models.TimeField(verbose_name='Время загрузки груза')),
                ('cargo_unloading_date', models.DateField(blank=True, null=True, verbose_name='Дата выгрузки груза')),
                ('cargo_unloading_time', models.TimeField(blank=True, null=True, verbose_name='Время выгрузки груза')),
                ('additional_requirements', models.TextField(blank=True, null=True, verbose_name='Дополнительные требования')),
                ('order_stage', models.CharField(choices=[('П', 'Принято'), ('О', 'Отказано'), ('В', 'В обработке')], default='В', max_length=1, verbose_name='Стутус заказы')),
                ('adding_datetime', models.DateTimeField(auto_now=True, verbose_name='Дата и время добавления заказа')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to=settings.AUTH_USER_MODEL, verbose_name='Заказчик')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('adding_datetime', 'cargo_name'),
            },
        ),
    ]