from django.shortcuts import render, redirect
from user_profile.models import UserInfo, User
from .models import Refill
from .forms import RefillCreateForm



def refill_info(request):
    info=UserInfo.objects.filter(user=request.user)
    #user= User.objects.filter(pk=request.user.id)
    if request.method=='POST':
        form = RefillCreateForm(request.POST)
        if form.is_valid():
            refil=form.save()
            info = UserInfo.objects.get(pk=request.POST['info'])
            #user = User.objects.get(pk= request.POST['user.id'])
            refill = Refill.objects.create(info=info)

            return render(request, 'refill_submited.html', {'refill':refill, 'refil':refil})
    else:
        form = RefillCreateForm()
        return render(request,'refill_info_check.html',{'info':info,'form':form})
