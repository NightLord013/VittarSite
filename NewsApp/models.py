from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    create_date = models.DateField(verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-create_date',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
