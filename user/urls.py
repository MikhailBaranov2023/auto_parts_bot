from django.urls import path
from user.apps import UserConfig
from user.views import UserListAPIView, UserDeleteAPIView

app_name = UserConfig.name

urlpatterns = [
    path("list/", UserListAPIView.as_view(), name='users_list'),
    path('<int:pk>/', UserDeleteAPIView.as_view(), name='delete'),
]
