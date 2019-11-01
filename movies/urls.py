from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.genres),
    path('genres/<int:genre_pk>/', views.genre_detail),

]
