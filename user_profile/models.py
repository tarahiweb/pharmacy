from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.IntegerField(null=True)

class UserInfo(models.Model):
    user=models.ForeignKey(User,related_name='info')
    address = models.CharField(max_length=200)
    zip = models.CharField(max_length=20)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
