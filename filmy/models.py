from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=300)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmy'
