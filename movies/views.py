from django.shortcuts import render
from .models import Genre
from .serializers import GenreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def genres(request):
    genre_all = Genre.objects.all()
    serializer = GenreSerializer(genre_all, many=True)
    return Response(serializer.data)