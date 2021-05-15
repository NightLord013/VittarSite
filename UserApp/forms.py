from django import forms
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Почта'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'Пароль'}),
    )
    class Meta:
        model = User
        fields = ('username', 'password')


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('full_name', 'company_name', 'email', 'phone', 'password1', 'password2')
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'ФИО', 'autofocus': True}),
            'company_name': forms.TextInput(attrs={'placeholder': 'Название компании'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Почта'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон'}),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Пароль'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Повторить пароль'})