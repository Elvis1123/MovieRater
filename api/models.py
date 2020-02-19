from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=360)

    def __str__(self):
        return self.title

    def votes(self):
        return len(Rating.objects.filter(movie=self))

    '''def average_rate(self):
        ratings = Rating.objects.filter(movie=self)
        sum = 0
        for rate in ratings:
            sum +=rate.stars
        return sum / len(ratings)'''


class Rating(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE, related_name='rating')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    class Meta:
        unique_together = (('user','movie'),)
        index_together = (('user','movie'),)

    def __str__(self):
        return f"{self.user} has given {self.stars} stars to the {self.movie} movie"

    def movie_name(self):
        return self.movie.title