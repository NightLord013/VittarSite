from django.shortcuts import render

def home(request):
    """Гланая страница"""
    return render(request, 'OrderApp/home.html')