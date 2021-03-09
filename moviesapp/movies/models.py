# -*- coding: utf-8 -*-
from django.urls import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(_('Movie\'s title'), max_length=255, unique=True)
    year = models.PositiveIntegerField(default=2019)
    # Example: PG-13
    rated = models.CharField(max_length=64)
    released_on = models.DateField(_('Release Date'))
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    # Todo: add Rating models
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'id': self.pk})
    
    class Meta:
        ordering = ['-rating', '-released_on']
    

class Rating(models.Model):
    value = models.FloatField(default=0)
    comment = models.TextField(blank=True, null=True)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ratings')