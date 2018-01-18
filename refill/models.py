from django.db import models
from user_profile.models import UserInfo, User

class Refill(models.Model):
    #user = models.ForeignKey(User, related_name='refill')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    info = models.ForeignKey(UserInfo,null=True,related_name='infouser')
    Dr_name=models.CharField(max_length=50)
    Dr_Phone_number=models.IntegerField(null=True)
    Dr_adrress = models.CharField(max_length=100)
    last_pharmacy = models.CharField(max_length=100)
    last_pharmacy_adrress = models.CharField(max_length=100)
    drug_name= models.CharField(max_length=100)
    drug_dose  = models.CharField(max_length=20)
    prescription = models.ImageField(blank=True)
    more_refill = models.BooleanField(default=False)
    class Meta:
        ordering= ('-created',)

    def __str__(self):
        return 'Refill{}'.format(self.id)

