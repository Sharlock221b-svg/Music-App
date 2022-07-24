from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Artists(models.Model):
    """name, artist_photo (url), followers"""
    name = models.CharField(max_length=100,unique=True)
    artist_photo = models.URLField(max_length=500)
    followers = models.IntegerField(default=0)

    def __str__(self):
        return f"Singer {self.name}"

class Songs(models.Model):
    """name, artist fk Artists, song_file (file_field), image_url, likes, genre"""
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE, related_name="get_songs")
    song_file=models.FileField(upload_to='songs/')
    image_url = models.URLField(blank=True,max_length=500)
    likes = models.IntegerField(default=0)
    genre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name} by {self.artist.name}"


class Followers(models.Model):
    """artist fk Artists, user fk User"""
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE, related_name="get_followers")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_artists")

    def __str__(self):
        return f"{self.user.username} followes {self.artist.name}"

class Likes(models.Model):
    """liked_song fk Songs, user fk User"""
    liked_song = models.ForeignKey(Songs, on_delete=models.CASCADE, related_name="get_likers")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_liked_songs")

    def __str__(self):
        return f"{self.liked_song.name} liked by {self.user.username}"