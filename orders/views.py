from django.shortcuts import render, redirect
from user_profile.models import UserInfo
from .models import OrderItem,Order
from cart.cart import Cart
from pharmacy.report import render_to_pdf
import braintree
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse,reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from . import forms
from pharmacy import settings
from django.utils.translation import ugettext_lazy as _
from .forms import    CheckoutForm
from django.http import HttpResponse
from django.conf import settings
from decimal import Decimal
from django.core.mail import send_mail
from django.template.loader import render_to_string

def order_info(request):
    user=request.user
    info=UserInfo.objects.filter(user=request.user)
    cart = Cart(request)
    total = 0
    for item in cart:
        total+=(item['price']* int(item['quantity']))
    total= str(total)
    if request.method=='POST':
        info = UserInfo.objects.get(pk=request.POST['info'])
        order = Order.objects.create(info=info)
        order.shiping_method=request.POST['shiping_method']
        order.save()
        request.session['order.id'] = order.id
        for item in cart:
            OrderItem.objects.create(order=order,
                                     drug=item['drug'],
                                      price=item['price'],
                                     quantity=item['quantity'])

            cart.clear()
        return redirect(reverse('order:checkout'))
        #return reverse_lazy('orders:checkout',kwargs={'pk':pk})
        #return render(request, 'orders/checkout.html', {'order': order})
    else:

        return render(request,'orders/info-chek.html',{'info':info,'cart':cart,'user':user, 'total':total})


"""
Adds simple form view, which communicates with Braintree.

There are four steps to finally process a transaction:

1. Create a client token (views.py)
2. Send it to Braintree (js)
3. Receive a payment nonce from Braintree (js)
4. Send transaction details and payment nonce to Braintree (views.py)

"""

class CheckoutView(generic.FormView):
    """This view lets the user initiate a payment."""
    form_class = forms.CheckoutForm
    template_name = 'orders/checkout.html'
    success_url = 'order:checkout-successful'

    #def total_amount(self):
     #   request=self.request
      #  order_id = request.session['order.id']
        #order= Order.objects.get(pk = order_id)
        #amount = order.get_total_cost()
        #shipment = Decimal(order.shiping_method)
        #total_amount = amount + shipment
        #return render(request, {'total_amount':total_amount})


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # We need the user to assign the transaction
        self.user = request.user
        # Ha! There it is. This allows you to switch the
        # Braintree environments by changing one setting
        if settings.BRAINTREE_PRODUCTION:
            braintree_env = braintree.Environment.Production
        else:
            braintree_env = braintree.Environment.Sandbox

        # Configure Braintree
        braintree.Configuration.configure(
            braintree_env,
            merchant_id=settings.BRAINTREE_MERCHANT_ID,
            public_key=settings.BRAINTREE_PUBLIC_KEY,
            private_key=settings.BRAINTREE_PRIVATE_KEY,
        )

        # Generate a client token. We'll send this to the form to
        # finally generate the payment nonce
        # You're able to add something like ``{"customer_id": 'foo'}``,
        # if you've already saved the ID
        self.braintree_client_token = braintree.ClientToken.generate({})
        return super(CheckoutView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        request = self.request
        order_id = request.session['order.id']
        order = Order.objects.get(pk=order_id)
        amount = order.get_total_cost()
        shipment = Decimal(order.shiping_method)
        total_amount = (amount + shipment)
        ctx = super(CheckoutView, self).get_context_data(**kwargs)
        ctx.update({
            'braintree_client_token': self.braintree_client_token,
            'total_amount':total_amount,
            'order':order,
            'amount':amount,
        })
        return ctx

    def form_valid(self, form):
        # Braintree customer info
        # You can, for sure, use several approaches to gather customer infos
        # For now, we'll simply use the given data of the user instance
        customer_kwargs = {
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "email": self.user.email,

        }

        # Create a new Braintree customer
        # In this example we always create new Braintree users
        # You can store and re-use Braintree's customer IDs, if you want to
        result = braintree.Customer.create(customer_kwargs)
        if not result.is_success:
            # Ouch, something went wrong here
            # I recommend to send an error report to all admins
            # , including ``result.message`` and ``self.user.email``

            context = self.get_context_data()
            # We re-generate the form and display the relevant braintree error
            context.update({
                'form': self.get_form(self.get_form_class()),
                'braintree_error': u'{} {}'.format(
                    result.message, _('Please get in contact.'))
            })
            return self.render_to_response(context)
        # If the customer creation was successful you might want to also
        # add the customer id to your user profile
        customer_id = result.customer.id
        """
        Create a new transaction and submit it.
        I don't gather the whole address in this example, but I can
        highly recommend to do that. It will help you to avoid any
        fraud issues, since some providers require matching addresses

        """
        address_dict = {
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "street_address":"300 E longleaf dr",
            "extended_address": 'auburn',
            "locality": 'auburn',
            #"region": 'state_or_region',
            "postal_code": '36832',
            #"country_code_alpha2": 'alpha2_country_code',
            #"country_code_alpha3": 'alpha3_country_code',
            #"country_name": 'country',
            #"country_code_numeric": 'numeric_country_code',
        }
        # You can use the form to calculate a total or add a static total amount
        # I'll use a static amount in this example
        request = self.request
        order_id = request.session['order.id']
        order = Order.objects.get(pk=order_id)
        amount = order.get_total_cost()
        shipment = Decimal(order.shiping_method)
        total_amount = amount + shipment
        result = braintree.Transaction.sale({
            "customer_id": customer_id,
            "amount": total_amount,
            "payment_method_nonce": form.cleaned_data['payment_method_nonce'],
            "descriptor": {
                #Definitely check out https://developers.braintreepayments.com/reference/general/validation-errors/all/python#descriptor
                "name": "COMPANY*test",

           },
            "billing": address_dict,
            "shipping": address_dict,
            "options": {
                # Use this option to store the customer data, if successful
                'store_in_vault_on_success': True,
                # Use this option to directly settle the transaction
                # If you want to settle the transaction later, use ``False`` and later on
                # ``braintree.Transaction.submit_for_settlement("the_transaction_id")``
                'submit_for_settlement': True,
            },
        })
        if not result.is_success:
            # Card could've been declined or whatever
            # I recommend to send an error report to all admins
            # , including ``result.message`` and ``self.user.email``

            context = self.get_context_data()
            context.update({
                'form': self.get_form(self.get_form_class()),
                'braintree_error': _(
                   'Your payment could not be processed. Please check your'
                    ' input or use another payment method and try again.')
            })
            return self.render_to_response(context)

        # Finally there's the transaction ID
        # You definitely want to send it to your database
        transaction_id = result.transaction.id
        # Now you can send out confirmation emails or update your metrics
        # or do whatever makes you and your customers happy :)
        order.paid = True
        order.save()
        # report
        pdf = render_to_pdf('report/shop-report.html', {'order':order,'total':total_amount})  # todo send fax and sms and email
        # email
        msg = render_to_string('email/shop-factor.html',
                               {'order': order,
                                'total':total_amount})
        send_mail('Thank you', 'your order is successfuly submited',
                  settings.DEFAULT_FROM_EMAIL, [self.request.user.email], fail_silently=False,html_message=msg),
        return super(CheckoutView, self).form_valid(form)

    def get_success_url(self):
        return reverse(self.success_url)


def Checkout_Successfull(request):
    return render(request, 'orders/created.html')

