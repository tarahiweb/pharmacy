from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,null=True)



class UserInfo(models.Model):
    user= models.ForeignKey(User,related_name='info')
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
    parrent=models.ForeignKey(Question, related_name='answer')
    body = models.TextField()
    user=models.ForeignKey(User,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self):
        message = 'answer to your question \n {answer}'.format(answer=self.body)
        msg_html = render_to_string('email/one_text.html',
                                    {'text': message})
        send_mail('answer to your question', 'answer to your question',
                  settings.DEFAULT_FROM_EMAIL, [self.parrent.user.email], fail_silently=False, html_message=msg_html),



