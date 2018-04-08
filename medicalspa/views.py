from django.shortcuts import render, redirect, HttpResponse
from user_profile.models import UserInfo, User
from .forms import CompoundCreateForm, Coumpound_not_logged_in_form
from django.http import HttpResponse
from .models import Compound,Compound_Drug
from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartADDDrugForm


def compound_info(request):

    if request.user.is_authenticated:
        info=UserInfo.objects.filter(user=request.user)
        #user= User.objects.filter(pk=request.user.id)
        if request.method=='POST':
            form = CompoundCreateForm(request.POST)
            if form.is_valid():
                compound = form.save(commit=False)
                information = UserInfo.objects.get(pk=request.POST['info'])
                compound.info = information
                compound.save()
                for i in range(int(request.POST['drug_num'])):
                    drug = Compound_Drug.objects.create(drug_name=request.POST['drug_name_{}'.format(i + 1)],
                                           drug_dose=request.POST['drug_dose_{}'.format(i + 1)], med=compound)

                return render(request, 'medicalspa/compound-submited.html', {'refill':compound})
            return HttpResponse(form.errors)
        else:
            form = CompoundCreateForm()
            return render(request,'medicalspa/compound-check-info.html',{'info':info,'form':form})
    else:
        if request.method == "POST":
            form= Coumpound_not_logged_in_form(request.POST)
            if form.is_valid():
                compound= form.save(commit=False)
                compound.save()
                for i in range(int(request.POST['drug_num'])):
                    drug = Compound_Drug.objects.create(drug_name=request.POST['drug_name_{}'.format(i + 1)],
                                           drug_dose=request.POST['drug_dose_{}'.format(i + 1)], med=compound)
                return render(request, 'medicalspa/compound-submited.html', {'refill': compound})
            return HttpResponse(form.errors)
        else:
            form = Coumpound_not_logged_in_form()
            return render(request, 'medicalspa/not_loged_in_compounding_info.html', {'form': form})

