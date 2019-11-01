from django.shortcuts import render, get_object_or_404
from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer, ReviewSerializer
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

@api_view(['POST'])
def review_create(request, movie_pk):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie_pk)
        # movie_id로 넣어줘야 하는 이유 : db_sqlite3에 movie_id라고 저장되었기 때문
        return Response({'message': "작성되었습니다."})
        # 입력할 때 {"content": "_", "score": 1, "movie": 1} 이 양식으로 데이터를 넣어줘야 한다.