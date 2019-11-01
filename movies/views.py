from django.shortcuts import render, get_object_or_404
from .models import Genre
from .serializers import GenreSerializer
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