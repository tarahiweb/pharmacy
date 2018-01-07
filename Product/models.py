from django.db import models


class  Drug(models.Model):
    drug_name = models.CharField(max_length=1000)
    dose = models.CharField(max_length=1000)
    drug_company = models.CharField(max_length=1000)
    drug_pic = models.CharField(max_length=1000)
    description  = models.CharField(max_length=1000)
    drug_usage = models.CharField(max_length=1000)
    def __str__(self):
        return self.drug_name+ ' , ' + self.dose
