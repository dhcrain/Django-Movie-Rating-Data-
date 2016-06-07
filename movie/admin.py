from django.contrib import admin
from movie.models import Rater
from movie.models import Rating
from movie.models import Movie


# Register your models here.
admin.site.register(Rater)
admin.site.register(Rating)
admin.site.register(Movie)
