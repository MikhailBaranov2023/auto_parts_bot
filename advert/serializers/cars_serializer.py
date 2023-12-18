from rest_framework.serializers import ModelSerializer
from advert.models import Car
from advert.models import CarImageGallery


class CarImagesSerializer(ModelSerializer):
    class Meta:
        model = CarImageGallery
        fields = '__all__'


class CarsSerializer(ModelSerializer):
    images_gallery = CarImageGallery

    class Meta:
        model = Car
        fields = "__all__"
