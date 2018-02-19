from django.db import models
from Product.models import Drug
from user_profile.models import UserInfo

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    sent=models.BooleanField(default=False)
    shiping_method_choices =(
        ('e == 7.5', 'express one day shiping $7.5'),
        ('r == 0', 'regular three day shiping'  ),
    )
    shiping_method=models.CharField(choices=shiping_method_choices,default='r', max_length=50)
    info = models.ForeignKey(UserInfo,null=True,related_name='info')
    class Meta:
        ordering= ('-created',)

    def __str__(self):
        return 'Order{}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    drug = models.ForeignKey(Drug, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

