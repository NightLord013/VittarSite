from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http.response import HttpResponse

def all_news(request):
    """Все новости компании"""
    news = News.objects.all()
    paginator = Paginator(news, 3)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # Если переданная страница не является числом, возвращаем первую
        news = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # Если получили AJAX - запрос с номером страницы, большим, чем их количество,
            # возвращаем пустую страницу.
            return HttpResponse('')
        # Если номер страницы больше, чем их количество, возвращаем последнюю.
        news = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request, 'NewsApp/all_news_ajax.html', {'news': news})
    return render(request, 'NewsApp/all_news.html', {'news': news})

