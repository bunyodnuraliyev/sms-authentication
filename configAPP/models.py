from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Actor(models.Model):
    name = models.CharField(max_length=15, blank=True, null=True)
    birthdate = models.DateField()


class Movie(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    year = models.DateField()
    actor = models.ManyToManyField('Actor')


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    create_date = models.DateField(auto_now_add=True)
