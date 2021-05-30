from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from .models import User
from OrderApp.models import Order

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'UserApp/registration.html'

def profile(request):
    user = User.objects.get(email=request.user)
    order_count = Order.objects.filter(user=user)
    return render(request, 'UserApp/profile.html', {'user': user, 'order_count': order_count})

