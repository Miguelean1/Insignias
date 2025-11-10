from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField()
    last_name = models.CharField()
    year_of_birth = models.IntegerField()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField(max_length=1000)
    GENRES = [
        ('AC', 'Action'),
        ('DR', 'Drama'),
        ('CO', 'Comedy'),
        ('SF', 'Sci-Fi'),
        ('HO', 'Horror')
    ]
    genre = models.CharField(max_length=2, choices=GENRES)
    director = models.CharField(max_length=100)
    release_year = models.IntegerField(validators=[MinValueValidator(1900)])
    duration = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(500)])
    release_date = models.DateField()
    announcement_date = models.DateField()
    has_subtitles = models.BooleanField()
    subtitles_language = models.CharField(blank=True)
    imdb = models.URLField(blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True, null=True)
    actors = models.ManyToManyField(Actor, blank=True)

    def clean(self):
        super().clean()
        errores = {}
        if self.announcement_date > self.release_date:
            errores["announcement_date"] = "The announcement date must be before the release date"
        if self.has_subtitles and not self.subtitles_language:
            errores["subtitles_language"] = "Please specify a language"
        if errores:
            raise ValidationError(errores)