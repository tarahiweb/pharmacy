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

    def add(self, drug, quantity=1, update_quantity=False ):
        drug_id = str(drug.id)
        if drug_id not in self.cart:
            self.cart[drug_id]= {'quantity':0}
        if update_quantity:
            self.cart[drug_id]['quantity']= quantity
        else:
            self.cart[drug_id]['quantity']+= quantity
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
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True