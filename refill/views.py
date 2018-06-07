from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.template.loader import render_to_string
from pharmacy.report import render_to_pdf
from user_profile.models import UserInfo
from pharmacy.twilio import send_fax
from .models import Refill, Drug, NewRx, Drug_refill,DrugQeust,NewRxAsQeust
from django.forms import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import braintree
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views import generic
from . import forms
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal

@login_required(login_url='user_profile:login')
def new_rx(request):
    info=UserInfo.objects.filter(user=request.user)
    #user= User.objects.filter(pk=request.user.id)
    if request.method=='POST':
        form = forms.NewRxForm(request.POST,request.FILES)
        if form.is_valid():
            newrx = form.save(commit=False)
            information = UserInfo.objects.get(pk=request.POST['info'])
            newrx.info = information
            newrx.save()
            request.session['refill.id'] = newrx.id
            for i in range(int(request.POST['drug_num'])):
                drug = Drug.objects.create(drug_name=request.POST['drug_name_{}'.format(i + 1)],
                                           drug_dose=request.POST['drug_dose_{}'.format(i + 1)], med=newrx)

            drugs = Drug.objects.filter(med=newrx)

            contect = {
                'refill': newrx,
                'drug': drugs,
            }
            # email

            message='Your order is successfully submited, we will notify you as soon as we verify it'
            msg_html = render_to_string('email/one_text.html',
                                        {'text': message })
            send_mail(message, message,
                      settings.DEFAULT_FROM_EMAIL, [request.user.email], fail_silently=False, html_message=msg_html),

            # return HttpResponse(pdf, content_type='application/pdf')
            send_fax('https://www.tysonspharmacy.us/refill/report/NewRx/')
            return render(request, 'refill/refill_submited.html', {'refill':newrx})
        return render(request, 'refill/new_rx.html', {'info': info, 'form': form})
    else:
        form = forms.NewRxForm()
        return render(request, 'refill/new_rx.html', {'info':info, 'form':form})


def report_newRx(request):
    info = UserInfo.objects.filter(user=request.user)
    order = NewRx.objects.filter(info=info)
    order=order.first()
    drug= Drug.objects.filter(med=order)
    print(drug)
    pdf = render_to_pdf('report/refill-report.html', {'refill':order, "drug":drug})
    return HttpResponse(pdf, content_type='application/pdf')


@csrf_exempt
def ajax(request):

    if request.method=='POST':
        reserve = {
            'days': 'ok',
        }
    else:
        reserve = {
            'days': 'not',
        }
    return JsonResponse(reserve)



@login_required(login_url='user_profile:login')
def refill_objects_list(request):
    order=NewRx.objects.filter(info__user=request.user).filter(verified=True)
    return render(request, 'one_click_refill/one_click_refill.html', {'order':order})

def refill_submit(request, pk):
    if request.method=='GET':
        info = UserInfo.objects.filter(user=request.user)
        rx=get_object_or_404(NewRx,pk=pk)
        current_user=request.user
        if not current_user==rx.info.user:
            messages.info(request,'you are not allow here')
            return render(request, 'user_profile/user-message.html')
        else:
            if rx.verified!=True:
                messages.info(request,'this order is not verified yet')
                return render(request, 'user_profile/user-message.html')
            return render(request, 'one_click_refill/one_click_refill_submit.html', {'rx':rx, 'info':info})

    else:
        order=get_object_or_404(NewRx,pk=pk)
        drug=order.drug_set.all().count()
        order.pk=None
        order.info=UserInfo.objects.get(pk=request.POST['info'])
        order.refill=True
        order.verified=False
        order.save()
        for i in range(drug):
            if not request.POST['drug_pk{}'.format(i + 1)]=='':
                drug=Drug.objects.get(pk=request.POST['drug_pk{}'.format(i + 1)])
                drug.pk=None
                drug.med=order
                drug.save()
        drug=Drug.objects.filter(med=order)
        contect = {
            'refill': order,
            'drug': drug,
        }
        pdf = render_to_pdf('report/refill-report.html', contect)  # todo send fax

        # emai

        message = 'Your Refill has been submitted successfully, we will notify you as soon as your order get verified'
        msg_html = render_to_string('email/one_text.html',
                                    {'text': message})
        send_mail(message, message,
                  settings.DEFAULT_FROM_EMAIL, [request.user.email], fail_silently=False, html_message=msg_html),

        messages.info(request, 'you refill order successfully submited')
        return render(request, 'user_profile/user-message.html')




def NewRx_checkout(request, **kwargs):
    user = request.user
    info = UserInfo.objects.filter(user=request.user)
    newrx = NewRx.objects.get(pk=kwargs['pk'])
    drug = newrx.drug_set.all()
    if request.method=='POST':
        newrx.shiping_method= request.POST['shiping_method']
        newrx.save()
        request.session['newrx.id'] = newrx.id
        return redirect(reverse('refill:newrx-checkoutview'))
    else:

        return render(request,'refill/newrx_checkout.html',{'info':info,'user':user, 'drug':drug, 'newrx':newrx})



# payment sectoin
class NewRx_CheckoutView(generic.FormView):
    """This view lets the user initiate a payment."""
    form_class = forms.NewRx_CheckoutForm
    template_name = 'refill/NewRx_Chechout_payment.html'
    success_url = 'refill:new-rx-checkout-successful'

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
        return super(NewRx_CheckoutView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        request = self.request
        newrx_id = request.session['newrx.id']
        newrx = NewRx.objects.get(pk=newrx_id)
        drug = newrx.drug_set.all()
        total = 0
        for item in drug:
            total += item.drug_price
        amount = Decimal(total) + Decimal(newrx.shiping_method)
        ctx = super(NewRx_CheckoutView, self).get_context_data(**kwargs)
        ctx.update({
            'braintree_client_token': self.braintree_client_token,
            'newrx':newrx,
            'drug':drug,
            'amount':amount
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
        newrx_id = request.session['newrx.id']
        newrx = NewRx.objects.get(pk=newrx_id)
        drug = newrx.drug_set.all()
        total = 0
        for item in drug:
            total += item.drug_price
        amount = Decimal(total) + Decimal(newrx.shiping_method)
        result = braintree.Transaction.sale({
            "customer_id": customer_id,
            "amount": amount,
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
        message = 'Thank you, your payment was successfull'
        msg_html = render_to_string('email/one_text.html',
                                    {'text': message})
        send_mail(message, message,
                  settings.DEFAULT_FROM_EMAIL, [self.request.user.email], fail_silently=False, html_message=msg_html),
        newrx.paid = True
        newrx.save()
        return super(NewRx_CheckoutView, self).form_valid(form)

    def get_success_url(self):
        return reverse(self.success_url)


def Checkout_Successfull(request):
    return render(request, 'refill/NewRx_checkout_successful.html')


# qeust views

def refill_as_qeust(request):
    #info=UserInfo.objects.filter(user=request.user)
    #user= User.objects.filter(pk=request.user.id)
    if request.method=='POST':
        form = forms.RefillForm(request.POST)
        if form.is_valid():
            refill = form.save(commit=False)
            refill.save()
            for i in range(int(request.POST['drug_num'])):
                drug = Drug_refill.objects.create(drug_name=request.POST['drug_name_{}'.format(i + 1)],
                                           drug_dose=request.POST['drug_dose_{}'.format(i + 1)], med=refill)

            drugs = Drug_refill.objects.filter(med=refill)
            contect = {
                'refill': refill,
                'drug': drugs,
            }
            # email

            message = 'Your order is successfully submited, we will notify you as soon as we verify it'
            msg_html = render_to_string('email/one_text.html',
                                        {'text': message})
            send_mail(message, message,
                      settings.DEFAULT_FROM_EMAIL, [refill.Email], fail_silently=False, html_message=msg_html),
            sid=send_fax('https://www.tysonspharmacy.us/refill/report/refill-as-guest/')
            print(sid.sid)
            # return HttpResponse(pdf, content_type='application/pdf')
            return render(request, 'refill/refill_submited.html', {'refill':refill})
        return render(request, 'refill/refill_as_qeust.html', {'form': form})
        #return HttpResponse(form.errors)
    else:
        form = forms.RefillForm()
        return render(request, 'refill/refill_as_qeust.html', {'form':form})

def report_refill_asguest(request):
    #info = UserInfo.objects.filter(user=request.user)
    order=Refill.objects.first()
    drug= Drug_refill.objects.filter(med=order)
    pdf = render_to_pdf('report/rport-refill-asguest.html', {'refill':order, "drug":drug})
    return HttpResponse(pdf, content_type='application/pdf')


def newrx_as_qeust(request):
    #info=UserInfo.objects.filter(user=request.user)
    #user= User.objects.filter(pk=request.user.id)
    if request.method=='POST':
        form = forms.NewRxAsGeustForm(request.POST,request.FILES)
        if form.is_valid():
            rx_qeust = form.save(commit=False)
            rx_qeust.save()
            for i in range(int(request.POST['drug_num'])):
                drug = DrugQeust.objects.create(drug_name=request.POST['drug_name_{}'.format(i + 1)],
                                           drug_dose=request.POST['drug_dose_{}'.format(i + 1)], med=rx_qeust)

            drugs = DrugQeust.objects.filter(med=rx_qeust)
            contect = {
                'refill': rx_qeust,
                'drug': drugs,
            }
            # email

            message = 'Your order is successfully submited, we will notify you as soon as we verify it'
            msg_html = render_to_string('email/one_text.html',
                                        {'text': message})

            send_mail(message, message,settings.DEFAULT_FROM_EMAIL,[rx_qeust.email], fail_silently=False, html_message=msg_html),

            pdf = render_to_pdf('report/refill-report.html', contect)
            # return HttpResponse(pdf, content_type='application/pdf')
            sid = send_fax('https://www.tysonspharmacy.us/refill/report/NewRx-as-guest/')
            print(sid.sid)
            return render(request, 'refill/refill_submited.html', {'refill':rx_qeust})
        return render(request, 'refill/newrx_as_qeust.html', {'form': form})
        #return HttpResponse(form.errors)
    else:
        form = forms.NewRxAsGeustForm()
        return render(request, 'refill/newrx_as_qeust.html', {'form':form})


def report_newRx_asguest(request):
    #info = UserInfo.objects.filter(user=request.user)
    order=NewRxAsQeust.objects.first()
    drug= DrugQeust.objects.filter(med=order)
    pdf = render_to_pdf('report/report-newrx-as-guest.html', {'refill':order, "drug":drug})
    return HttpResponse(pdf, content_type='application/pdf')