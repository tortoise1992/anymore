from django.db import models
from django.urls import reverse
# Create your models here.
class User(models.Model):
    userName=models.CharField(max_length=30)
    userPhone=models.CharField(max_length=11)
    userPwd=models.CharField(max_length=10)

class Category(models.Model):
    name=models.CharField(max_length=100)

class Tag(models.Model):
    name=models.CharField(max_length=100)

class Post(models.Model):
    title=models.CharField(max_length=70)
    body=models.TextField()
    create_time=models.DateTimeField()
    update_time=models.DateTimeField()
    excerpt=models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
        # print(self.pk)