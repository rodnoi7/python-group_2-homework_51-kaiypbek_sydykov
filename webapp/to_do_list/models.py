from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Наименование')
    status = models.CharField(max_length=30, null=False, blank=False, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return '%s: статус - %s(создана: %s)' % (self.name, self.status, self.created_at)