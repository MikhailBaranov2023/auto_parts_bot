from django.db import models
from user.models import User

NULLABLE = {'blank': True, 'null': True}


class Car(models.Model):
    owner = models.ForeignKey(User, verbose_name='Владелец авто', on_delete=models.CASCADE, **NULLABLE)
    mark = models.CharField(max_length=50, verbose_name='марка', **NULLABLE)
    model = models.CharField(max_length=50, verbose_name='модель', **NULLABLE)
    description = models.TextField(max_length=1000, verbose_name='описание', **NULLABLE)
    year = models.CharField(max_length=50, verbose_name='год выпуска', **NULLABLE)
    sale = models.BooleanField(default=False, verbose_name='на продажу', **NULLABLE)
    disassembly = models.BooleanField(default=False, verbose_name='авто в разборе', **NULLABLE)
    image = models.CharField(verbose_name='фото', **NULLABLE)

    class Meta:
        verbose_name = "машина"
        verbose_name_plural = 'машины'


class Request(models.Model):
    owner = models.ForeignKey(User, verbose_name='создатель запроса', on_delete=models.CASCADE, **NULLABLE)
    mark_auto = models.CharField(max_length=50, verbose_name='марка автомобиля', **NULLABLE)
    model_auto = models.CharField(max_length=50, verbose_name='модель автомобиля', **NULLABLE)
    year_auto = models.CharField(max_length=50, verbose_name='год выпуска авто', **NULLABLE)
    description = models.CharField(max_length=300, verbose_name='описание', **NULLABLE)
    part = models.BooleanField(default=False, verbose_name='запрос на запчасть', **NULLABLE)
    unit = models.BooleanField(default=False, verbose_name='запрос на агрегат', **NULLABLE)
    photo = models.ImageField(verbose_name='фото', **NULLABLE)

    class Meta:
        verbose_name = "запрос"
        verbose_name_plural = "запросы"


class Request_To_Repair(models.Model):
    owner = models.ForeignKey(User, verbose_name='создатель запроса на ремонт', on_delete=models.CASCADE, **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='город', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='описание', **NULLABLE)

    class Meta:
        verbose_name = "запрос на ремонт"
        verbose_name_plural = "запросы на ремонт"
