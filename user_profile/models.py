from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.IntegerField(null=True)

    # class UserProfile(models.Model):
    # user = models.OneToOneField(User)
    # first_name = User.first_name
    # last_name = User.last_name
    # email = User.email
    # def __unicode__(self):
    #   return self.user.username

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def Create_profile(sender, instance, created, **kwargs):
    if created:
        profile, new = User.objects.get_or_create(user=instance)


class UserInfo(models.Model):
    user=models.ForeignKey(User,related_name='info')
    address = models.CharField( max_length=200)
    zip = models.CharField(max_length=20)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username



class Question(models.Model):
    user=models.ForeignKey(User,blank=True,null=True)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'Question :'+ self.body

class Answer(models.Model):
    parrent=models.ForeignKey(Question, related_name='child')
    user = models.ForeignKey(User, blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'reply on : ' + self.body


#class UserProfile(models.Model):
    #user = models.OneToOneField(User)
    #first_name = User.first_name
    #last_name = User.last_name
    #email = User.email
    #def __unicode__(self):
     #   return self.user.username

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender= User)
def Create_profile(sender, instance, created, **kwargs):
    if created:
        profile, new = User.objects.get_or_create(user = instance)





