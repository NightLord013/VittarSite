from django.shortcuts import render, redirect
from .models import Order
from UserApp.models import User
from .forms import OrderForm
from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    """Гланая страница"""
    return render(request, 'OrderApp/home.html')

@login_required
def user_orders(request):
    """Заказы пользователя"""
    user = request.user
    orders = Order.objects.filter(user=user).order_by('-adding_datetime')
    return render(request, 'OrderApp/user_orders.html', {'orders': orders})


def order_form(request):
    """Страница заказа услуги"""
    if request.method == 'POST':
        form = OrderForm(request.POST, initial={'user': request.user})
        if form.is_valid():
            form.save()
            return redirect('user_orders')
    else:
        form = OrderForm(initial={'user': request.user})
    return render(request, 'OrderApp/order_form.html', {'form': form})

@user_passes_test(lambda user: user.is_staff)
def all_orders(request):
    """Все заказы пользователей"""
    orders = Order.objects.filter(order_stage='В').order_by('-adding_datetime')
    return render(request, 'OrderApp/all_orders.html', {'orders': orders})

@user_passes_test(lambda user: user.is_staff)
def order_accept(request, order_id):
    order = Order.objects.get(id=order_id)
    order.order_stage = 'П'
    order.save()
    return redirect('all_orders')

@user_passes_test(lambda user: user.is_staff)
def order_deny(request, order_id):
    order = Order.objects.get(id=order_id)
    order.order_stage = 'О'
    order.save()
    return redirect('all_orders')