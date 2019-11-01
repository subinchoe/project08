from rest_framework import serializers
from .models import Genre, Movie, Review

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content', 'score', 'movie',)

class GenreDetailSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(source="movie_set", many=True)
    class Meta:
        model = Genre
        fields = ('id', 'movies', 'name')