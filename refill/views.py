from django.shortcuts import render, HttpResponse

from pharmacy.report import render_to_pdf
from user_profile.models import UserInfo
from .forms import NewRxForm, RefillForm
from .models import Refill, Drug, NewRx, Drug_refill
from django.forms import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



def new_rx(request):
    info=UserInfo.objects.filter(user=request.user)
    #user= User.objects.filter(pk=request.user.id)
    if request.method=='POST':
        form = NewRxForm(request.POST,request.FILES)
        if form.is_valid():
            refill = form.save(commit=False)
            information = UserInfo.objects.get(pk=request.POST['info'])
            refill.info = information
            refill.save()
            for i in range(int(request.POST['drug_num'])):
                drug = Drug.objects.create(drug_name=request.POST['drug_name_{}'.format(i + 1)],
                                           drug_dose=request.POST['drug_dose_{}'.format(i + 1)], med=refill)

            drugs = Drug.objects.filter(med=refill)
            drugs = Drug.objects.filter(med=refill)
            contect = {
                'refill': refill,
                'drug': drugs,
            }
            return HttpResponse(refill.verify_optin)
            pdf = render_to_pdf('report/refill-report.html', contect)
            return HttpResponse(pdf, content_type='application/pdf')
            return render(request, 'refill_submited.html', {'refill':refill})
        print(form.errors)

        return render(request, 'new_rx.html', {'info': info, 'form': form})
    else:
        form = NewRxForm()
        return render(request, 'new_rx.html', {'info':info, 'form':form})



def report(request):
    refill=NewRx.objects.last()
    drug=Drug.objects.filter(med=refill)
    contect={
        'refill':refill,
        'drug':drug
    }
    pdf=render_to_pdf('report/refill-report.html',contect)
    return HttpResponse(pdf,content_type='application/pdf')


@csrf_exempt
def ajax(request):

    if request.method=='POST':
        reserve = {
            'days': 'ok',
        }
    else:
        reserve = {
            'days': 'not',
        }
    return JsonResponse(reserve)



def refill(request):
    info=UserInfo.objects.filter(user=request.user)
    #user= User.objects.filter(pk=request.user.id)
    if request.method=='POST':
        form = RefillForm(request.POST,request.FILES)
        if form.is_valid():
            refill = form.save(commit=False)
            information = UserInfo.objects.get(pk=request.POST['info'])
            refill.info = information
            refill.save()
            for i in range(int(request.POST['drug_num'])):
                drug = Drug_refill.objects.create(drug_name=request.POST['drug_name_{}'.format(i + 1)],
                                           drug_dose=request.POST['drug_dose_{}'.format(i + 1)], med=refill)

            drugs = Drug_refill.objects.filter(med=refill)
            contect = {
                'refill': refill,
                'drug': drugs,
            }
            return HttpResponse(refill.verify_optin)
            pdf = render_to_pdf('report/refill-report.html', contect)
            return HttpResponse(pdf, content_type='application/pdf')
            return render(request, 'refill_submited.html', {'refill':refill})
        return HttpResponse(form.errors)
        return render(request, 'new_rx.html', {'info': info, 'form': form})
    else:
        form = RefillForm()
        return render(request, 'Refill.html', {'info':info, 'form':form})
