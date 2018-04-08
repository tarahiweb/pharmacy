from django.db import models
from django.core.urlresolvers import reverse
from user_profile.models import User, UserInfo
class Compound(models.Model):
    #user = models.ForeignKey(User, related_name='refill')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    info = models.ForeignKey(UserInfo,null=True,related_name='compoundinfo')
    #Medical_spa_name=models.CharField(max_length=50)
    Phone_number=models.IntegerField(null=True)
    First_name = models.CharField(max_length=50, null=True)
    Last_name =models.CharField(max_length=50, null=True)
    Email_address = models.EmailField(blank=True,null=True)
    State= models.CharField(max_length=50,blank=True,null=True)
    City = models.CharField(max_length=50,blank=True,null=True)
    Zip = models.CharField(max_length=5,blank=True,null=True)

    class Meta:
        ordering= ('-created',)

    def __str__(self):
        return 'Compound{}'.format(self.id)

    #def userinfo_address(self):
     #   return self.info.address
    #userinfo_address.short_description = 'user Address'

    #def userinfo_city(self):
     #   return self.info.city
    #userinfo_city.short_description = 'user City'

    #def userinfo_zip(self):
        #return self.info.zip
    #userinfo_zip.short_description = 'user zip'

class Compound_Drug(models.Model):
    med=models.ForeignKey(Compound,null=True)
    drug_name = models.CharField(max_length=100)
    drug_dose = models.CharField(max_length=20)
    drug_percentage= models.CharField(max_length=20)
