from rest_framework import generics
from user.models import User
from user.serializers import UserSerializer


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
