from django.db import models
from django.contrib.auth.models import User

class Band(models.Model):
    name = models.CharField(max_length=100)

class Album(models.Model):
    name = models.CharField(max_length=100)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

class Song(models.Model):
    name = models.CharField(max_length=100)
    duration = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.DecimalField(max_digits=3, decimal_places=1)

class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
    content = models.TextField()

class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
