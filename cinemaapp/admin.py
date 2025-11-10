from django.contrib import admin

from cinemaapp.models import Actor, Movie

# Register your models here.
admin.site.register(Movie)
admin.site.register(Actor)