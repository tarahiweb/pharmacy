from django.shortcuts import render
from user_profile.form import LoginForm
def Home(request):
    return render(request,'home/home.html')


def Privacy(request):
    return render(request, 'home/privacy.html')


def Terms(request):
    return render(request, 'home/terms.html')

def test(request):
    form=LoginForm()
    return render(request,'home/test.html')