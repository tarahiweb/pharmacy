from django.db import models
from django.core.urlresolvers import reverse
from user_profile.models import User


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
    user=models.ForeignKey(User,blank=True,null=True)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    drug_slug=models.SlugField(allow_unicode=True)
    def __str__(self):
        return 'comment on '+ self.post_slug

class ChildComment(models.Model):
    parrent=models.ForeignKey(Comment,related_name='child')
    user = models.ForeignKey(User, blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    drug_slug = models.SlugField(allow_unicode=True)

    def __str__(self):
        return 'reply on ' + self.post_slug
