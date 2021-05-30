from django import forms
from .models import Order
from django.contrib.admin import widgets

class OrderForm(forms.ModelForm):
    """Форма заказа услуги"""
    class Meta:
        model = Order
        exclude = ('order_stage',)
        widgets = {
            'user': forms.HiddenInput(),
            'cargo_volume': forms.NumberInput(attrs={'value': 0}),
            'cargo_weight': forms.NumberInput(attrs={'value': 0}),
            'distance': forms.NumberInput(attrs={'value': 0}),
            'cargo_loading_date': forms.NumberInput(attrs={'type': 'date'}),
            'cargo_loading_time': forms.NumberInput(attrs={'type': 'time'}),
            'cargo_unloading_date': forms.NumberInput(attrs={'type': 'date'}),
            'cargo_unloading_time': forms.NumberInput(attrs={'type': 'time'}),
        }