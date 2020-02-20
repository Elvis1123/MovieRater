from rest_framework import serializers
from .models import Movie,Rating
from django.contrib.auth.models import User

'''class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [ 'username']'''

class RatinSerilazier(serializers.ModelSerializer):
    '''user = UserSerializer(many=False)'''

    class Meta:
        model = Rating
        fields = ['id', 'stars','user','movie']


class MovieSerializer(serializers.ModelSerializer):
    rating = RatinSerilazier(many=True)

    class Meta:

        model = Movie
        fields = ['id','title', 'description','votes','rating','average_rate']





