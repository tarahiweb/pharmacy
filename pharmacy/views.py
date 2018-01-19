from django.shortcuts import render

def Home(request):
    return render(request,'home/home.html')


def Privacy(request):
    return render(request, 'home/privacy.html')


def Terms(request):
    return render(request, 'home/terms.html')