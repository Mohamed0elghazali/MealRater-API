from rest_framework import serializers

from .models import Meal, Rating

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'meal_name', 'description']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'stars', 'user', 'meal'] 