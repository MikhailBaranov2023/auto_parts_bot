from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}


class User(models.Model):
    username = models.CharField(unique=True, max_length=50, verbose_name='username')
    first_name = models.CharField(max_length=50, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name='фамилия', **NULLABLE)
    phone = models.CharField(max_length=50, verbose_name='номер телефона', unique=True, **NULLABLE)
    subscription = models.BooleanField(default=False, verbose_name='подписка')
    date_from = models.DateField(verbose_name='дата началаподписки', **NULLABLE)
    date_to = models.DateField(verbose_name='дата окончания пописки', **NULLABLE)

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
