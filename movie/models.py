from django.db import models

# Create your models here.


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return str(self.occupation)


class Movie(models.Model):
    movie_title = models.CharField(max_length=50)
    release_date = models.CharField(max_length=15)
    video_release_date = models.CharField(max_length=15, default="")      # empty is OK
    imdb_url = models.CharField(max_length=300)
    unknown = models.CharField(max_length=50)
    action = models.BooleanField()
    adventure = models.BooleanField()
    animation = models.BooleanField()
    childrens = models.BooleanField()
    comedy = models.BooleanField()
    crime = models.BooleanField()
    documentry = models.BooleanField()
    drama = models.BooleanField()
    fantasy = models.BooleanField()
    film_noir = models.BooleanField()
    horror = models.BooleanField()
    musical = models.BooleanField()
    mystery = models.BooleanField()
    romance = models.BooleanField()
    sci_fi = models.BooleanField()
    thriller = models.BooleanField()
    war = models.BooleanField()
    western = models.BooleanField()

    def __str__(self):
        return self.movie_title


class Rating(models.Model):
    user_id = models.ForeignKey(Rater)
    # OR user_id = models.ForeignKey("movie.Rater")  ("app_name.Class")
    item_id = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.item_id)
