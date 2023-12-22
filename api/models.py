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
    
    def no_of_ratings(self):
        all_ratings = Rating.objects.filter(meal=self)
        return len(all_ratings)
    
    def avg_ratings(self):
        all_ratings = Rating.objects.filter(meal=self)

        sum_all_ratings = 0
        no_all_ratings = 0

        for i in all_ratings:
            sum_all_ratings += i.stars
            no_all_ratings += 1

        if no_all_ratings == 0:
            return 0
        return sum_all_ratings / no_all_ratings
    
class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'Meal: {self.meal.meal_name}, Rating: {self.stars}'
    
    class Meta:
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal',))