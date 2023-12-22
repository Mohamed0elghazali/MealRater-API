from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

## read on uuid or slugs
class Meal(models.Model):
    meal_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.meal_name
    
class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'Meal: {self.meal.meal_name}, Rating: {self.stars}'
    
    class Meta:
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal',))