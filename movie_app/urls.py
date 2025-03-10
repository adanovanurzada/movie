from .views import *
from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout_list'),

    path('profiles/', ProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='profile-list'),
    path('profiles/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='profile-detail'),

    path('countries/', CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='country-list'),
    path('countries/<int:pk>/', CountryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='country-detail'),

    path('directors/', DirectorViewSet.as_view({'get': 'list', 'post': 'create'}), name='director-list'),
    path('directors/<int:pk>/', DirectorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='director-detail'),

    path('actors/', ActorViewSet.as_view({'get': 'list', 'post': 'create'}), name='actor-list'),
    path('actors/<int:pk>/', ActorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='actor-detail'),

    path('genres/', GenreViewSet.as_view({'get': 'list', 'post': 'create'}), name='genre-list'),
    path('genres/<int:pk>/', GenreViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='genre-detail'),

    path('movies/', MovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie-list'),
    path('movies/<int:pk>/', MovieViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='movie-detail'),

    path('movie-languages/', MovieLanguagesViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie-languages-list'),
    path('movie-languages/<int:pk>/', MovieLanguagesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='movie-languages-detail'),

    path('moments/', MomentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='moments-list'),
    path('moments/<int:pk>/', MomentsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='moments-detail'),

    path('ratings/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating-list'),
    path('ratings/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='rating-detail'),

    path('favorites/', FavoriteViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite-list'),
    path('favorites/<int:pk>/', FavoriteViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='favorite-detail'),

    path('favorite-movies/', FavoriteMovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite-movie-list'),
    path('favorite-movies/<int:pk>/', FavoriteMovieViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='favorite-movie-detail'),

    path('history/', HistoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='history-list'),
    path('history/<int:pk>/', HistoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='history-detail'),
]
