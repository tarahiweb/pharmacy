from django.db import models
from django.core.urlresolvers import reverse
from user_profile.models import User
from markdown_deux import markdown
from django.utils.safestring import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug =models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:product_list_by_category', args=[self.slug])





class  Drug(models.Model):
    category= models.ForeignKey(Category,null=True , related_name='products')
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
    drug_type=models.CharField(max_length=100, blank=True)
    over_the_counter = models.BooleanField(default=False)
    drug_ingredient = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta :
        ordering = ('created', )


    def __str__(self):
        return self.drug_name+ ' , ' + self.dose

    def get_absolute_url(self):
        return reverse("product:detail",kwargs={"drug_slug": self.slug})

    def get_markdown(self):
        content = self.description
        markdown_text = markdown(content)
        return mark_safe(markdown_text)

class Comment(models.Model):
    user=models.ForeignKey(User,blank=True,null=True)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    drug_slug=models.SlugField(allow_unicode=True)
    def __str__(self):
        return 'comment on '+ self.drug_slug

class ChildComment(models.Model):
    parrent=models.ForeignKey(Comment,related_name='child')
    user = models.ForeignKey(User, blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    drug_slug = models.SlugField(allow_unicode=True)

    def __str__(self):
        return 'reply on ' + self.drug_slug
