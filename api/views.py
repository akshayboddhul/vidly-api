from rest_framework import generics, permissions

from rest_framework_simplejwt.authentication import JWTAuthentication

from movies.models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer


class MovieCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    # print("Tokee", authentication_classes)


class MovieUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class GenreCreateAPIView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
