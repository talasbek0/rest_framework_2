from django.urls import path, include, re_path
from .views import TourListViewSet, AboutListViewSet, ReviewListViewSet, CustomTourRequestViewSet
from RentCar.views import RentCarVIEWSet, CarsVIEWSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'TourList', TourListViewSet, basename='guaranteed-tours')
router.register(r'About', AboutListViewSet, basename='about')
router.register(r'Rent of Car', RentCarVIEWSet, basename='Renting')
router.register(r'Cars', CarsVIEWSet, basename='Cars')
router.register(r'Review', ReviewListViewSet, basename='Review')
router.register(r'CustomRequest', CustomTourRequestViewSet, basename='CustomRequest')

urlpatterns = [
    path('', include(router.urls)),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    #http://127.0.0.1:8000/api/token/
    path('api/token/', obtain_auth_token, name='token_obtain_pair'),
]