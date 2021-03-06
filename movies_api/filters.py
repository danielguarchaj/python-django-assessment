from django_filters import rest_framework as filters
from moviesapp.movies.models import Movie

class MovieFilter(filters.FilterSet):
  class Meta:
    model = Movie
    fields = {
      "title": ["icontains"],
    }