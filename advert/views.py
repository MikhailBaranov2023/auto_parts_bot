from rest_framework import generics
from advert.serializers.cars_serializer import CarsSerializer, CarImagesSerializer
from advert.models import Car, CarImageGallery


class CarUpdateDestroyRetrieveAPIView(generics.UpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView):
    """класс для редактирования, удаления и просмотра объявления о машине"""
    serializer_class = CarsSerializer
    queryset = Car.objects.all()


class CarCreateAPIView(generics.CreateAPIView):
    """класс для создания обявления о машине"""
    serializer_class = CarsSerializer
    queryset = Car.objects.all()

