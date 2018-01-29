from django.shortcuts import render, redirect, HttpResponse
from user_profile.models import UserInfo, User
from .models import Refill, Drug
from .forms import RefillCreateForm



def refill_info(request):
    info=UserInfo.objects.filter(user=request.user)
    #user= User.objects.filter(pk=request.user.id)
    if request.method=='POST':
        form = RefillCreateForm(request.POST)
        if form.is_valid():
            refill = form.save(commit=False)
            information = UserInfo.objects.get(pk=request.POST['info'])
            refill.info = information
            refill.save()
            for i in range(int(request.POST['drug_num'])):
                drug = Drug.objects.create(drug_name=request.POST['drug_name_{}'.format(i + 1)],
                                           drug_dose=request.POST['drug_dose_{}'.format(i + 1)], med=refill)

            return render(request, 'refill_submited.html', {'refill':refill})
        return render(request, 'refill_info_check.html', {'info': info, 'form': form})
    else:
        form = RefillCreateForm()
        return render(request,'refill_info_check.html',{'info':info,'form':form})
