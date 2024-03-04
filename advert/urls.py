from django.urls import path
from advert.views import CarCreateAPIView, CarApiView, CarListAPIView, RequestListAPIView, RequestDeleteAPIView, \
    RequestToRepairListAPIView, RequestToRepairDeleteAPIView
from advert.apps import AdvertConfig

app_name = AdvertConfig.name

urlpatterns = [
    path('car/create/', CarCreateAPIView.as_view(), name='car_create'),
    path('car/<int:pk>/', CarApiView.as_view(), name='cars_api'),
    path('cars/', CarListAPIView.as_view(), name='cars_list'),
    path('requests/', RequestListAPIView.as_view(), name='requsets_list'),
    path('request/delete/<int:pk>/', RequestDeleteAPIView.as_view(), name="delete_request"),
    path('requests_to_repair/', RequestToRepairListAPIView.as_view(), name='list_request_to_repair'),
    path('requests_to_repair/delete/<int:pk>/', RequestToRepairDeleteAPIView.as_view(),
         name='delete_request_to_repair'),

]
