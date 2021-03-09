from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import MovieSerializer, RatingSerializer
from .filters import MovieFilter

from moviesapp.movies.models import Movie, Rating

class MovieListCreateView(ListCreateAPIView):
    queryset = Movie.objects.all()
    filterset_class = MovieFilter
    serializer_class = MovieSerializer


class MovieRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    filterset_class = MovieFilter
    serializer_class = MovieSerializer


class RatingListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer