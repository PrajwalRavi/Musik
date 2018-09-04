from django.core import validators
from django.core.urlresolvers import reverse
from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=50)
    logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'album_id': self.id})

    def __str__(self):
        return self.album_title + " by " + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100)
    is_favourite = models.BooleanField(default=False)
    # the extension of song_file is checked to allow only mp3 files
    song_file = models.FileField(default=False,
                                 validators=[validators.FileExtensionValidator(allowed_extensions='mp3',
                                                                               message='Only mp3 files are allowed')])

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'album_id': self.album.id})

    def __str__(self):
        return self.song_title + "by" + self.album.artist
