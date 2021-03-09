from rest_framework import serializers

from moviesapp.movies.models import Movie, Rating
from django.db.models import Avg


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

    def create(self, validated_data):
        obj = Rating.objects.create(**validated_data)        
        
        movie_ratings = Rating.objects.filter(movie=obj.movie).aggregate(Avg('value'))
        
        obj.movie.rating = round(movie_ratings['value__avg'], 2)
        obj.movie.save()
        return obj