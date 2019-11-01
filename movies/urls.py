from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.genres),
    path('genres/<int:genre_pk>/', views.genre_detail),
    path('movies/', views.movies),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/reviews/', views.review_create),
]
