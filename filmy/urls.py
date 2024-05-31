from django.contrib import admin
from django.urls import path

from filmy import views

urlpatterns = [
    path('', views.movies, name='movies'),
    path('reziseri/', views.reziseri, name='reziseri'),
    path("film/<int:id>", views.movie, name="movie"),
]
