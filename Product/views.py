from django.http import HttpResponse
from .models import Drug
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404

def index(request):
    all_drug= Drug.objects.all()
    return render(request, 'Product/index.html', {'all_drug': all_drug})


def details(request, drug_id):
    drug = get_object_or_404(Drug, pk= drug_id)
    return render(request, 'Product/detail.html', {'drug': drug})
