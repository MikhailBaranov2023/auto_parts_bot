from django.urls import path
from advert.views import CarCreateAPIView, CarUpdateDestroyRetrieveAPIView
from advert.apps import AdvertConfig

app_name = AdvertConfig.name

urlpatterns = [
    path('cars/create/', CarCreateAPIView.as_view(), name='car_create'),
    path('cars/<int:pk>/', CarUpdateDestroyRetrieveAPIView.as_view(), name='car_api_view')
]