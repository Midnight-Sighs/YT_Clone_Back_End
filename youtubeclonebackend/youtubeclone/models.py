from django.db import models

# Create your models here.
class Comments(models.Model):
    videoId = models.TextField()
    content = models.CharField(max_length=150)
    like_counter = models.IntegerField(default=0)
    dislike_counter = models.IntegerField(default=0)
    

class Replies(models.Model):
    content = models.CharField(max_length= 150)
    comment = models.ForeignKey('Comments', on_delete=models.CASCADE,)