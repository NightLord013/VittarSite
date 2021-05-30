from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignInForm
from .views import SignUpView, profile

urlpatterns = [
    path('login/', LoginView.as_view(template_name='UserApp/login.html', authentication_form=SignInForm), name='login'),
    path('registration/', SignUpView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
]