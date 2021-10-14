from django.db import models

# Create your models here.
class Comments(models.Model):
    videoId = models.TextField(max_length=11)
    content = models.TextField(max_length=250)
    like_counter = models.IntegerField(default=0)
    dislike_counter = models.IntegerField(default=0)
    

class Replies(models.Model):
    content = models.TextField(max_length= 250)
    comment = models.ForeignKey('Comments', on_delete=models.CASCADE,)