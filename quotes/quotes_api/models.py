from django.db import models

# Create your models here.
from django.db import models

class Character(models.Model):
    name = models.TextField()

class TVShow(models.Model):
    name = models.TextField()

class Quote(models.Model):
    quote = models.TextField()
    season_number = models.IntegerField(null=True)
    episode_number = models.IntegerField(null=True)
    said_by = models.ForeignKey(Character, on_delete=models.CASCADE)
    tv_show = models.ForeignKey(TVShow, on_delete=models.CASCADE)
