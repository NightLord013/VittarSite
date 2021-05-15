from django.db import models
from django.conf import settings

ORDER_STAGE = (
    ('П', 'Принято'),
    ('О', 'Отказано'),
    ('В', 'В обработке')
)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='user_orders', verbose_name='Заказчик')
    departure_address = models.CharField(max_length=100, verbose_name='Адрес отправки')
    delivery_address = models.CharField(max_length=100, verbose_name='Адрес доствки')
    cargo_name = models.CharField(max_length=100, verbose_name='Описание груза')
    cargo_weight = models.IntegerField(verbose_name='Вес груза')
    cargo_volume = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Объем груза')
    cargo_loading_date = models.DateField(verbose_name='Дата загрузки груза') # ограничить выбор раньше сегодняшней даты!!
    cargo_loading_time = models.TimeField(verbose_name='Время загрузки груза')
    cargo_unloading_date = models.DateField(blank=True, null=True, verbose_name='Дата выгрузки груза')
    cargo_unloading_time = models.TimeField(blank=True, null=True, verbose_name='Время выгрузки груза')
    additional_requirements = models.TextField(blank=True, null=True, verbose_name='Дополнительные требования')
    order_stage = models.CharField(max_length=1, choices=ORDER_STAGE, default='В', verbose_name='Стутус заказы')
    adding_datetime = models.DateTimeField(auto_now=True, verbose_name='Дата и время добавления заказа')

    def __str__(self):
        return self.cargo_name

    class Meta:
        ordering = ('adding_datetime', 'cargo_name',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
