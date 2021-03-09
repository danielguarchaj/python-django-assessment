# -*- coding: utf-8 -*-
from django.urls import path, include

from . import views

urlpatterns = [
    path('movies/', views.MovieListCreateView.as_view(), name='movies_list_create'),
    path('movies/<int:pk>/', views.MovieRetrieveDestroyView.as_view(), name='movies_retrieve_destroy'),
    path('ratings/', views.RatingListCreateView.as_view(), name='ratings_list_create'),
]
