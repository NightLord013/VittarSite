from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('OrderApp.urls', namespace='')),
    path('account/', include('UserApp.urls')),
]
