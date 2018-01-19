from django.shortcuts import render, redirect
from user_profile.models import UserInfo, User
from .models import Emergency_Med
from .forms import Emergency_MedCreateForm



def Emergency_info(request):
    info=UserInfo.objects.filter(user=request.user)
    #user= User.objects.filter(pk=request.user.id)
    if request.method=='POST':
        form = Emergency_MedCreateForm(request.POST)
        if form.is_valid():
            emergency=form.save()
            info = UserInfo.objects.get(pk=request.POST['info'])
            #user = User.objects.get(pk= request.POST['user.id'])
            emergency_med = Emergency_Med.objects.create(info=info)

            return render(request, "emergency/emergency_submited.html", {'emergency_med':emergency_med, 'emergency':emergency})
    else:
        form = Emergency_MedCreateForm()
        return render(request,'emergency/emergency-check-info.html',{'info':info,'form':form})
