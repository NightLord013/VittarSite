from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'departure_address', 'delivery_address', 'cargo_name', 'order_stage', 'adding_datetime')
    fields = ('user', ('departure_address', 'delivery_address'), 'cargo_name', ('cargo_weight', 'cargo_volume'),
             ('cargo_loading_date', 'cargo_loading_time'), ('cargo_unloading_date', 'cargo_unloading_time'),
              'additional_requirements', 'order_stage')
    list_filter = ('order_stage',)
    search_fields = ('departure_address', 'delivery_address', 'cargo_name')
    date_hierarchy = 'adding_datetime'
