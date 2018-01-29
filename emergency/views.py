from django.shortcuts import render, redirect
from user_profile.models import UserInfo, User
from .models import Emergency_Med,Drug
from .forms import Emergency_MedCreateForm
from django.http import HttpResponse


def Emergency_info(request):
    info=UserInfo.objects.filter(user=request.user)
    #user= User.objects.filter(pk=request.user.id)
    if request.method=='POST':
        form = Emergency_MedCreateForm(request.POST)
        if form.is_valid():
            emergency=form.save(commit=False)
            info = UserInfo.objects.get(pk=request.POST['info'])
            emergency.info=info
            emergency.save()
            emergency.save()
            for i in range(int(request.POST['drug_num'])):
                drug=Drug.objects.create(drug_name=request.POST['drug_name_{}'.format(i+1)],drug_dose=request.POST['drug_dose_{}'.format(i+1)],med=emergency)
            return render(request, "emergency/emergency_submited.html", {'emergency_med':emergency, 'emergency':emergency})
        return render(request, 'emergency/emergency-check-info.html', {'info': info, 'form': form})
    else:
        form = Emergency_MedCreateForm()
        return render(request,'emergency/emergency-check-info.html',{'info':info,'form':form})
