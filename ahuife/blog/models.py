from django.db import models

# Create your models here.
class User(models.Model):
    userName=models.CharField(max_length=30)
    userPhone=models.CharField(max_length=11)
    userPwd=models.CharField(max_length=10)


