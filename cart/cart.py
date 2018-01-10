from decimal import Decimal
from django.conf import settings
from Product.models import Drug


class Cart(object):
    def __init__(self, request):
        self.session= request.session
        cart= self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[settings.CART_SESSION_ID]= {}
        self.cart = cart

    def add(self, drug, quantity, update_quantity):
        drug_id = str(drug.id)
        if drug_id not in self.cart:
            self.cart[drug_id]= {'quantity':1}
            self.status=False
        else:
            self.status=True
        if update_quantity:
            self.cart[drug_id]['quantity']= quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, drug):
        drug_id =str(drug.id)
        if drug_id in self.cart:
            del self.cart[drug_id]
        self.save()


    def __iter__(self):
        drug_id = self.cart.keys()
        drugs=Drug.objects.filter(id__in=drug_id)
        for drug in drugs:
            self.cart[str(drug.id)]['drug']= drug
        for item in self.cart.values():
            #item['price'] = Decimal(item['price'])
            #item['total_price'] = item['price'] * item['quantity']
            yield item

    def len(self):
        return sum(1 for item in self.cart.values())

    #def get_total_price(self):
        #return sum(Decimal(item['price']) * item['quantity']for item in self.cart.values())

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True