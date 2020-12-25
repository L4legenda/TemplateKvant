from django.db import models

class Person(models.Model):
    comments = models.CharField('Комментарий', max_length=500)
    email = models.EmailField('Введите свой email')

    def __str__(self):
        return self.comments

    class Meta:
        verbose_name='Запрос'
        verbose_name_plural='Запросы'