from django.urls import path
from . import views

urlpatterns = [
    # все пользователи
    path('', views.home, name='home'),
    path('orders/', views.user_orders, name='user_orders'),
    path('order_form/', views.order_form, name='order_form'),

    # администратор
    path('all_orders/', views.all_orders, name='all_orders'),
    path('order/accept/<int:order_id>/', views.order_accept, name='order_accept'),
    path('order/deny/<int:order_id>/', views.order_deny, name='order_deny'),
]