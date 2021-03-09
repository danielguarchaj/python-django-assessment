# -*- coding: utf-8 -*-
from django.urls import path, include

from . import api

urlpatterns = [
    path('movies/', api.MovieListCreateView.as_view(), name='movies_list_create'),
    path('movies/<int:pk>/', api.MovieRetrieveDestroyView.as_view(), name='movies_retrieve_destroy'),
    path('ratings/', api.RatingListCreateView.as_view(), name='ratings_list_create'),
]
