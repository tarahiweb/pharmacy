from django.db import models
from user_profile.models import UserInfo, User
from refill.api import Fda_search
from django.conf import settings
from django.core.mail import send_mail
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
import random
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError



class NewRx(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    first_name=models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    # user = models.ForeignKey(User, related_name='refill')
    Date_of_Birth= models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    delivered=models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    refill=models.BooleanField(default=False)
    cansel=models.BooleanField(default=False)
    info = models.ForeignKey(UserInfo, null=True, related_name='info_user')

    Dr_name = models.CharField(max_length=50, help_text="only required if verifying with dr is selected", blank=True)
    dr_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                                    null=True)
    Dr_adrress = models.CharField(max_length=100, blank=True)

    last_pharmacy = models.CharField(max_length=100, blank=True)
    last_pharmacy_adrress = models.CharField(max_length=100, blank=True)

    prescription = models.ImageField(blank=True)

    more_refill = models.BooleanField(default=False)
    more_refill_number = models.CharField(max_length=20, blank=True)

    rx_number = models.CharField(max_length=10, null=True)

    __original_verify = False

    def __init__(self, *args, **kwargs):
        super(NewRx, self).__init__(*args, **kwargs)
        self.__original_verify = self.verified
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Refill{}'.format(self.id)


    def save(self):
        if not self.__original_verify:
            if self.verified == True:
                msg = render_to_string('email/payment-for-rx.html',
                                       {'order': self,
                                        'total': sum(item.drug_price for item in self.drug_set.all())})
                send_mail('order has been verified', 'order has been verified', #TODO: make email template
                          settings.DEFAULT_FROM_EMAIL, [self.info.user.email], fail_silently=False),
        a=1
        while a == 1:
            code = 'rx{}'.format(random.randrange(1000, 100000))
            if not NewRx.objects.filter(rx_number=code).exists():
                self.rx_number = code
                a = 2
        super(NewRx, self).save()

class Drug(models.Model):
    med=models.ForeignKey(NewRx,null=True)
    drug_name = models.CharField(max_length=100,blank=True)
    drug_dose = models.CharField(max_length=20,blank=True)
    drug_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True,default=0)


class Refill(models.Model): #todo can we just delete this??
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    Date_of_Birth = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    delivered= models.BooleanField(default=False)
    info = models.ForeignKey(UserInfo,null=True,related_name='infouser')
    RX_number= models.CharField(max_length=20, blank=True, help_text="optional")
    more_refill = models.BooleanField(default=False)
    more_refill_number = models.CharField(max_length=20, blank=True)


    class Meta:
        ordering= ('-created',)

    def __str__(self):
        return 'Refill{}'.format(self.id)

    def save(self):
        if self.verified==True:
            send_mail('verified', 'verified', #todo type message
                      settings.EMAIL_BACKEND, [self.info.user.email], fail_silently=False),
        super(Refill, self).save()

class Drug_refill(models.Model): #todo and delete this?
    med=models.ForeignKey(Refill,null=True)
    drug_name = models.CharField(max_length=50, blank=True)
    drug_dose = models.CharField(max_length=20, blank=True)
    drug_price= models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

