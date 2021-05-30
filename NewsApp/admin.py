from django.contrib import admin
from NewsApp.models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date')
    search_fields = ('title', 'body')