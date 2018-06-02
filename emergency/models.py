from django.db import models
from user_profile.models import UserInfo
from django.core.mail import send_mail
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
import random
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.conf import settings



class Emergency_Med(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    info = models.ForeignKey(UserInfo,null=True,related_name='emergencyinfo')
    Dr_name=models.CharField(max_length=50)
    Dr_Phone_number=models.IntegerField(null=True)
    Dr_adrress = models.CharField(max_length=100)
    last_pharmacy = models.CharField(max_length=100)
    last_pharmacy_adrress = models.CharField(max_length=100)
    prescription = models.ImageField(blank=True)


    def __str__(self):
        return 'Emergency{}'.format(self.id)

    class Meta:
        ordering= ('-created',)


class Drug(models.Model):
    med=models.ForeignKey(Emergency_Med,null=True)
    drug_name = models.CharField(max_length=100)
    drug_dose = models.CharField(max_length=20)


class Emergency_as_guest(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    Date_of_Birth = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    Email = models.EmailField(null=True)
    Phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                                    null=True)

    class Meta:
        ordering= ('-created',)

    def __str__(self):
        return 'Emergency'.format(self.id)
    def save(self):
        if self.verified==True:
            send_mail('verified', 'verified',
                      settings.DEFAULT_FROM_EMAIL, [self.Email], fail_silently=False),
        super(Emergency_as_guest, self).save()

class Drug_emergency_drug(models.Model):
    med=models.ForeignKey(Emergency_as_guest,null=True)
    drug_name = models.CharField(max_length=50, blank=True)
    drug_dose = models.CharField(max_length=20, blank=True)
    drug_price= models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)