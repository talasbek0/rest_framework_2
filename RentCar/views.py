from .serializers import *
from .models import *
from rest_framework import viewsets


class RentCarVIEWSet(viewsets.ModelViewSet):
    queryset = RentCar.objects.all()
    serializer_class = RentCarSerializer


class CarsVIEWSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer