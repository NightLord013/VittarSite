from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order
from NewsApp.models import News
from .forms import OrderForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    """Гланая страница"""
    news = News.objects.all()[:2]
    return render(request, 'OrderApp/home.html', {'news': news})

@login_required
def user_orders(request):
    """Заказы пользователя"""
    user = request.user
    orders = Order.objects.filter(user=user).order_by('-adding_datetime')
    paginator = Paginator(orders, 3)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        # Если переданная страница не является числом, возвращаем первую
        orders =paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # Если получили AJAX - запрос с номером страницы, большим, чем их количество,
            # возвращаем пустую страницу.
            return HttpResponse('')
        # Если номер страницы больше, чем их количество, возвращаем последнюю.
        orders = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request, 'OrderApp/user_orders_ajax.html', {'orders': orders})
    return render(request, 'OrderApp/user_orders.html', {'orders': orders})


@login_required
def order_form(request):
    """Страница заказа услуги"""
    if request.method == 'POST':
        form = OrderForm(request.POST, initial={'user': request.user})
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_orders')
        else:
            print(form.errors)
    else:
        form = OrderForm(initial={'user': request.user})
    return render(request, 'OrderApp/order_form.html', {'form': form})

@user_passes_test(lambda user: user.is_staff)
def all_orders(request):
    """Все заказы пользователей"""
    orders = Order.objects.filter(order_stage='В').order_by('-adding_datetime')
    paginator = Paginator(orders, 3)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        # Если переданная страница не является числом, возвращаем первую
        orders = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # Если получили AJAX - запрос с номером страницы, большим, чем их количество,
            # возвращаем пустую страницу.
            return HttpResponse('')
        # Если номер страницы больше, чем их количество, возвращаем последнюю.
        orders = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request, 'OrderApp/all_orders_ajax.html', {'orders': orders})
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

def about_company(request):
    return render(request, 'OrderApp/about_company.html')

def contacts(request):
    return render(request, 'OrderApp/contacts.html')