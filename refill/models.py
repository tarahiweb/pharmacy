from django.db import models
from user_profile.models import UserInfo, User
from refill.api import Fda_search
from django.conf import settings
from django.core.mail import send_mail
from phonenumber_field.modelfields import PhoneNumberField





class Refill(models.Model):
    #user = models.ForeignKey(User, related_name='refill')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    info = models.ForeignKey(UserInfo,null=True,related_name='infouser')
    verify_with_DR= models.BooleanField(default=False)
    Dr_name=models.CharField(max_length=50, help_text="only required if verifying with dr is selected", blank=True)
    Dr_Phone_number=PhoneNumberField(blank=True)
    Dr_adrress = models.CharField(max_length=100, blank=True)
    vedrify_with_Pharmacy = models.BooleanField(default=False)
    last_pharmacy = models.CharField(max_length=100, blank=True)
    last_pharmacy_adrress = models.CharField(max_length=100, blank=True)
    verify_with_prescription = models.BooleanField(default=False)
    prescription = models.ImageField(blank=True)
    more_refill = models.BooleanField(default=False)
    more_refill_number = models.CharField(max_length=20, blank=True)
    delivery_choice= (
        ('p','pick-up'),
        ('d','deliver'),
    )
    choose_your_shipment_method= models.CharField(max_length=1, choices=delivery_choice,default='d')
    class Meta:
        ordering= ('-created',)

    def __str__(self):
        return 'Refill{}'.format(self.id)

    def save(self):
        if self.verified==True:
            send_mail('verified', 'verified',
                      settings.EMAIL_BACKEND, ['abedi.mehrad@yahoo.com'], fail_silently=False),
        super(Refill, self).save()


    #def userinfo_address(self):
     #   return self.info.address
    #userinfo_address.short_description = 'user Address'

    #def userinfo_city(self):
     #   return self.info.city
    #userinfo_city.short_description = 'user City'

    #def userinfo_zip(self):
        #return self.info.zip
    #userinfo_zip.short_description = 'user zip'

class Drug(models.Model):
    med=models.ForeignKey(Refill,null=True)
    drug_name = models.CharField(max_length=100)
    drug_dose = models.CharField(max_length=20)
