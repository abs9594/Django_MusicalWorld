from django.db import models
from django.conf import settings


class Album(models.Model):

    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    language = models.CharField(max_length=250)
    album_logo = models.FileField()

    def __str__(self):
        return '{}'.format(self.album_title)


class Song(models.Model):

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    song_title = models.CharField(max_length=250)
    song_logo = models.ImageField(upload_to="images/")
    song_file = models.FileField(upload_to="songs/")

    def __str__(self):
        return '{}'.format(self.song_title)


class Playlist(models.Model):

    playlist_name = models.CharField(max_length=250)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return '{}'.format(self.playlist_name)




