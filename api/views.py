from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(methods=['post'], detail=True)
    def rate_meal(self, request, pk=None):
        ## check first if the stars exist in request data.
        if 'stars' in request.data:

            # query the Meal and Rating models with the coming data
            # get the meal using pk in url 
            meal = Meal.objects.get(pk = pk)

            # get data from request body
            username = request.data['username']
            stars = request.data['stars']

            # get the user model from query by username
            user = User.objects.get(username=username)

            # create or update ratings
            try:
                # update
                rating = Rating.objects.get(meal=meal.id, user=user.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)

                json = {
                    'Message': 'Rating is updated successfully.',
                    'Data': serializer.data,
                }
                return Response(json, status = status.HTTP_202_ACCEPTED)
            except:
                # create
                rating = Rating.objects.create(meal=meal, user=user, stars=stars)
                serializer = RatingSerializer(rating, many=False)

                json = {
                    'Message': 'Rating is created successfully.',
                    'Data': serializer.data,
                }
                return Response(json, status = status.HTTP_201_CREATED)
        else:
            json = {
                'Message': 'Stars does not exist in request',
            }
            return Response(json, status = status.HTTP_400_BAD_REQUEST)




class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
