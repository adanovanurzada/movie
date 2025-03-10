from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from .models import *
from .serializers import *
from .filters import MovieFilters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer


    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(date=request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)



class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request: Request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        try:
            serializers.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializers.validated_data
        return Response(serializers.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, reguest, *args, **kwargs):
        try:
            refresh_token =reguest.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_402_PAYMENT_REQUIRED)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilters
    search_fields = ['movie_name']
    ordering_fields = ['year']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MovieLanguagesViewSet(viewsets.ModelViewSet):
    queryset = MovieLanguages.objects.all()
    serializer_class = MovieLanguagesSerializer

class MomentsViewSet(viewsets.ModelViewSet):
    queryset = Moments.objects.all()
    serializer_class = MomentsSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteMovieViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteMovieSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

