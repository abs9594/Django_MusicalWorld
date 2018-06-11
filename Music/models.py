from django.db import models
from django.urls import reverse
from django.conf import settings

class Album(models.Model):

    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_logo = models.FileField()

    def __str__(self):
        return '{} {}'.format(self.album_title,self.artist)

class Song(models.Model):

    album = models.ForeignKey(Album , on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.song_title)

class Playlist(models.Model):

    name = models.CharField(max_length=250)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return '{}'.format(self.name)




