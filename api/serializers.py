from rest_framework import serializers
from .models import Movie, Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class RatinSerilazier(serializers.ModelSerializer):
    # user = UserSerializer(many=False)

    class Meta:
        model = Rating
        fields = ['id', 'stars', 'user', 'movie']


class MovieSerializer(serializers.ModelSerializer):
    # rating = RatinSerilazier(many=True)

    class Meta:
        # ,'rating'

        model = Movie
        fields = ['id', 'title', 'description', 'average_rate', 'votes']
