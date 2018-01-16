from django.shortcuts import render, redirect
from user_profile.models import UserInfo, User
from .models import Refill
from .forms import RefillCreateForm



def refill_info(request):
    info=UserInfo.objects.filter(user=request.user)
    user= User.objects.filter(pk=request.user.id)
    if request.method=='POST':
        info = UserInfo.objects.get(pk=request.POST['infouser'])
        user = User.objects.get(pk= request.POST['refill'])
        refill = Refill.objects.create(info=info,user=user)

        return render(request, 'refill_submited.html', {'refill':refill})
    else:
        return render(request,'refill_info_check.html',{'info':info,'user':user})
