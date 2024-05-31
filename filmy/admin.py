from django.contrib import admin

from filmy.models import Movie, Director, Genre, Actor

class ActorAdmin(admin.ModelAdmin):
    pass

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year', 'genres_display', 'director']
    list_display_links = ['name', 'id']
    search_fields = ['name', 'director__name']
    list_filter = ['genres', 'director']

class DirectorAdmin(admin.ModelAdmin):
    pass

class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)

admin.site.register(Director, DirectorAdmin)

admin.site.register(Genre, GenreAdmin)

admin.site.register(Actor, ActorAdmin)

# Register your models here.