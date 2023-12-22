from django.contrib import admin

from .models import Meal, Rating

## superuser ---> admin -- admin
## regularuser ---> dev -- dev12345
## regularuser ---> test -- dev12345



## to add filter to rating models in admin panel 
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'meal', 'user', 'stars']
    list_filter = ['meal', 'user']

## to add filter and search 
class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'meal_name', 'description']
    search_fields = ['meal_name', 'description']
    list_filter = ['meal_name', 'description']
 

admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)