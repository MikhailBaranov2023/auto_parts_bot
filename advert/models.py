from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Car(models.Model):
    mark = models.CharField(max_length=50, verbose_name='марка', **NULLABLE)
    model = models.CharField(max_length=50, verbose_name='модель', **NULLABLE)
    description = models.TextField(max_length=1000, verbose_name='описание', **NULLABLE)

    class Meta:
        verbose_name = "машина"
        verbose_name_plural = 'машины'


class CarImageGallery(models.Model):
    car = models.ForeignKey(Car, verbose_name='авто', on_delete=models.CASCADE)
    image_1 = models.ImageField(verbose_name='фото', **NULLABLE)
    image_2 = models.ImageField(verbose_name='фото', **NULLABLE)
    image_3 = models.ImageField(verbose_name='фото', **NULLABLE)
    image_4 = models.ImageField(verbose_name='фото', **NULLABLE)
    image_5 = models.ImageField(verbose_name='фото', **NULLABLE)

    class Meta:
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'
