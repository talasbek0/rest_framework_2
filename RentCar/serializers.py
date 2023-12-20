from rest_framework import serializers
from .models import RentCar, Cars


class RentCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentCar
        fields = '__all__'


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'