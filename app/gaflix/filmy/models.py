from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(blank=True, null=True)
    footage = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    main_picture = models.CharField(blank=True, default="", max_length=2000)
    director = models.ForeignKey('Director', on_delete=models.CASCADE, blank=True, null=True)
    actors = models.ManyToManyField('Actor', blank=True)
    genres = models.ManyToManyField('Genre', blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmy'

    def genres_display(self):
        return ', '.join([genre.name for genre in self.genres.all()])

class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    main_picture = models.ImageField()

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

class Actor(models.Model):
    name = models.CharField(max_length=300, null=True)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    main_picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
