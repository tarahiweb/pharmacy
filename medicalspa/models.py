from django.db import models
from django.core.urlresolvers import reverse
from user_profile.models import User, UserInfo


class  Drug(models.Model):
    drug_name = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)
    drug_company = models.CharField(max_length=100)
    drug_pic = models.ImageField(blank=True)
    description  = models.TextField(blank=True)
    drug_usage = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock= models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    slug = models.SlugField(unique=True, allow_unicode=True,null=True)

    def __str__(self):
        return self.drug_name+ ' , ' + self.dose

    def get_absolute_url(self):
        return reverse("product:detail",kwargs={"drug_slug": self.slug})


class Comment(models.Model):
    user=models.ForeignKey(User,blank=True,null=True, related_name='usercomment')
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    drug_slug=models.SlugField(allow_unicode=True)
    def __str__(self):
        return 'comment on '+ self.drug_slug

class ChildComment(models.Model):
    parrent=models.ForeignKey(Comment,related_name='spachild')
    user = models.ForeignKey(User, blank=True, related_name='userchildcomment')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    drug_slug = models.SlugField(allow_unicode=True)

    def __str__(self):
        return 'reply on ' + self.drug_slug



class Compound(models.Model):
    #user = models.ForeignKey(User, related_name='refill')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    info = models.ForeignKey(UserInfo,null=True,related_name='compoundinfo')
    Medical_spa_name=models.CharField(max_length=50)
    Phone_number=models.IntegerField(null=True)
    #delivery_choice= (
     #   ('p','pick-up'),
     #   ('d','deliver'),
    #)
    #choose_your_shipment_method= models.CharField(max_length=1, choices=delivery_choice,default='p')
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
