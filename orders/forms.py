from django import forms
from .models import Order
from cart.cart import Cart
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal

class CheckoutForm(forms.Form):
    payment_method_nonce = forms.CharField(
        max_length=1000,
        widget=forms.widgets.HiddenInput,
        required=False,  # In the end it's a required field, but I wanted to provide a custom exception message
    )
    amount= forms.DecimalField(max_digits=10, decimal_places=2,)



    def clean(self):
        self.cleaned_data = super(CheckoutForm, self).clean()
        # Braintree nonce is missing
        if not self.cleaned_data.get('payment_method_nonce'):
            raise forms.ValidationError(_(
                'We couldn\'t verify your payment. Please try again.'))
        return self.cleaned_data


    def amount_to_pay(self, request):
        order_id = request.session.get['order_id']
        order = Order.objects.get(pk= order_id)
        self.initial['amount']= order.get_total_cost()



