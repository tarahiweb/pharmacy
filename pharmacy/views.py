from django.shortcuts import render
from user_profile.form import LoginForm
from django.conf import settings
from django.core.mail import send_mail
from Product.models import Drug
from orders.models import Order
from refill.models import NewRx
from django.http import HttpResponse
from django.db.models import Sum
from decimal import Decimal
def Home(request):
    drug=Drug.objects.all()[:4]
    return render(request,'home/home.html',{'drug':drug})


def Privacy(request):
    return render(request, 'home/privacy.html')


def Terms(request):
    return render(request, 'home/terms.html')

def test(request):
    send_mail('ok', 'ok',
              settings.DEFAULT_FROM_EMAIL, ['abedi.mehrad@yahoo.com'], fail_silently=False),
    # order=NewRx.objects.last()
    # sumation=sum(item.drug_price for item in order.drug_set.all())
    # return HttpResponse(sumation)
    return render(request,'email/payment-for-rx.html')

