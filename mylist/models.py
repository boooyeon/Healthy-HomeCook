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
    

class Profile(models.Model):
    user = models.TextField()
    image = models.ImageField(upload_to="mylist/uploads")      # upload_to로 어디에 업로드할지 지정할 수 있음. # 하나의 사진은 한명의 사용자에게 속해야 하므로. 1:N의 관계
    # thumbnail_image = models.ImageField(blank=True)      # blank가 True이면 폼 입력시 꼭 입력하지 않아도 된다는 의미
    comment = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)  # 사용자가 입력하지 않고 업로드 하는 순간 자동으로 세팅이 됨.
    is_public = models.BooleanField(default=False)   