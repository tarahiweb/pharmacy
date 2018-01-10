from django.db import models
from django.core.urlresolvers import reverse

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

    def __str__(self):
        return self.drug_name+ ' , ' + self.dose

    def get_absolute_url(self):
        return reverse("product:detail",kwargs={"drug_id": self.id})