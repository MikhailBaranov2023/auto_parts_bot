from rest_framework.serializers import ModelSerializer
from advert.models import Car, Request, Request_To_Repair
from user.serializers import UserSerializer


class RequestToRepairSerializer(ModelSerializer):
    owner = UserSerializer

    class Meta:
        model = Request_To_Repair
        fields = '__all__'


class RequestSerializer(ModelSerializer):
    owner = UserSerializer

    class Meta:
        model = Request
        fields = "__all__"


class CarsSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
