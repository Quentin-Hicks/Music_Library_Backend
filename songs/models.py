from platform import release
from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField()
    artist = models.CharField()
    album = models.CharField()
    release_date = models.DateField()
    genre = models.CharField()