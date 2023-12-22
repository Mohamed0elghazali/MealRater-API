from django.urls import include, path
from rest_framework import routers
from .views import MealViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register('meals', MealViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]