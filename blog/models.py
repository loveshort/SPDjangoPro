from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) #标题
    content = models.TextField() #具体的问题信息
    pub_time = models.DateTimeField(auto_now_add=True) #发布时间
    author = models.CharField(max_length=100) #作者
    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()  #具体的文字信息
    pub_time = models.DateTimeField(auto_now_add=True) #发布时间
    author = models.CharField(max_length=100) #作者