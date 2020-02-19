from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import MovieSerializer,RatinSerilazier
from .models import Movie,Rating
from django.contrib.auth.models import User

class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatinSerilazier
    queryset = Rating.objects.all()



class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            #user = request.user
            user =User.objects.get(id=1)
            print('user',user.username)
            print(pk)
            response = {'message': 'It\'s working'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

