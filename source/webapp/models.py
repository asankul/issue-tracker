from django.db import models

# Create your models here.


class ToDo(models.Model):
    class Meta:
        verbose_name_plural = "ToDo lists"
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Текст')
    status = models.ForeignKey('Status', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус', related_name='list')
    type = models.ForeignKey('Type', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Тип', related_name='list')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.summary


class Status(models.Model):
    class Meta:
        verbose_name_plural = "Statuses"
    name = models.CharField(max_length=20, verbose_name='Статус')

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=20, verbose_name='Тип')

    def __str__(self):
        return self.name
