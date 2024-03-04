from rest_framework import generics
from advert.serializers.cars_serializer import CarsSerializer, RequestSerializer, RequestToRepairSerializer
from advert.models import Car, Request, Request_To_Repair


class CarCreateAPIView(generics.CreateAPIView):
    serializer_class = CarsSerializer
    queryset = Car.objects.all()


class CarListAPIView(generics.ListAPIView):
    serializer_class = CarsSerializer
    queryset = Car.objects.all()


class CarApiView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = CarsSerializer
    queryset = Car.objects.all()


class RequestListAPIView(generics.ListAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()


class RequestDeleteAPIView(generics.DestroyAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()


class RequestToRepairListAPIView(generics.ListAPIView):
    serializer_class = RequestToRepairSerializer
    queryset = Request_To_Repair.objects.all()


class RequestToRepairDeleteAPIView(generics.DestroyAPIView):
    serializer_class = RequestToRepairSerializer
    queryset = Request_To_Repair.objects.all()
