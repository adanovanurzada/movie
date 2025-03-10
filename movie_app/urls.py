from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', ProfileViewSet, basename='profiles'),
router.register(r'country', CountryViewSet, basename='countries'),
router.register(r'director', DirectorViewSet, basename='directors'),
router.register(r'actor', ActorViewSet, basename='actors'),
router.register(r'genre', GenreViewSet, basename='genres'),
router.register(r'favorite', FavoriteViewSet, basename='favorites'),
router.register(r'history', HistoryViewSet, basename='histories')


urlpatterns = [
    path('', include(router.urls)),
    path('movie/', MovieListAPIView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout _list')
]
