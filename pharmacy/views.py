from django.shortcuts import render
from user_profile.form import LoginForm
from django.conf import settings
from django.core.mail import send_mail
from Product.models import Drug

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

    return render(request,'email/one_text.html')

