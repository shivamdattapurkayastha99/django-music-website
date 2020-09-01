from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Song(models.Model):
    song_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    singer=models.CharField(max_length=20)
    tags=models.CharField(max_length=100)
    image=models.ImageField(upload_to='documents/media')
    song=models.FileField(upload_to='documents/media')
    movie=models.CharField(max_length=20,default="")
    def __str__(self):
        return self.name
class Watchlater(models.Model):
    watch_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    video_id=models.CharField(max_length=20,default="")
    