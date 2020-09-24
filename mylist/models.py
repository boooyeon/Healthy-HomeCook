# from django.db import models

from django.db import models

# Create your models here.
class Channel(models.Model):
    objects = models.Manager()
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    food_name = models.TextField()
    video_title= models.CharField(max_length=100)
    video_link = models.TextField()
   


class Cart(models.Model):
    user_id = models.TextField()
    ch_name= models.TextField()
    title= models.CharField(max_length=100)
    link = models.TextField()
    