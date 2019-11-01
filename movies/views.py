from django.shortcuts import render, get_object_or_404
from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def genres(request):
    genre_all = Genre.objects.all()
    serializer = GenreSerializer(genre_all, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, id=genre_pk)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)

@api_view(['GET'])
def movies(request):
    movie_all = Movie.objects.all()
    serializer = MovieSerializer(movie_all, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, id=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)