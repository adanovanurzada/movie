from django.contrib import admin
from .models import *

class MovieLanguageInline(admin.TabularInline):
    model = MovieLanguages
    extra = 1

class MomentsInline(admin.TabularInline):
    model = Moments
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieLanguageInline, MomentsInline]


admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(FavoriteMovie)
admin.site.register(History)


