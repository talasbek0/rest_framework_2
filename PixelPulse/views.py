from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from rest_framework.views import APIView


class MyProtectedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, ]


class TourListViewSet(viewsets.ModelViewSet):
    serializer_class = TourListSerializer
    queryset = TourList.objects.all()


class AboutListViewSet(viewsets.ModelViewSet):
    serializer_class = AboutSerializer
    queryset = About.objects.all()


class ReviewListViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class CustomTourRequestViewSet(viewsets.ModelViewSet):
    serializer_class = CustomTourRequestSerializer
    queryset = CustomTourRequest.objects.all()


