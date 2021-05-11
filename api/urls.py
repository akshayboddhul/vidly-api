from django.urls import path
from .views import MovieCreateAPIView, MovieUpdateAPIView, GenreCreateAPIView, GenreUpdateAPIView

urlpatterns = [
    path("movies/", MovieCreateAPIView.as_view()),
    path("movie/<int:pk>/", MovieUpdateAPIView.as_view()),

    path("genres/", GenreCreateAPIView.as_view()),
    path("genre/<int:pk>/", GenreUpdateAPIView.as_view()),
]
