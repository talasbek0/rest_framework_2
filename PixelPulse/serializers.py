from .models import *
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('author', 'text', 'rating', 'tour')


class TourListSerializer(serializers.ModelSerializer):
    title = serializers.CharField(help_text='Название Тура')
    description = serializers.CharField(help_text='Опишите тура')
    next_day = serializers.IntegerField(help_text='Продлинность')
    price = serializers.DecimalField(help_text='Цена $ ', max_digits=10, decimal_places=2)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = TourList
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('title', 'text')


class CustomTourRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomTourRequest
        fields = '__all__'