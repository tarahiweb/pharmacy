from django.shortcuts import render, HttpResponse, get_object_or_404

from pharmacy.report import render_to_pdf
from user_profile.models import UserInfo
from .forms import NewRxForm, RefillForm
from .models import Refill, Drug, NewRx, Drug_refill
from django.forms import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages


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

            # pdf = render_to_pdf('report/refill-report.html', contect)
            # return HttpResponse(pdf, content_type='application/pdf')
            return render(request, 'refill/refill_submited.html', {'refill':refill})
        print(form.errors)

        return render(request, 'refill/new_rx.html', {'info': info, 'form': form})
    else:
        form = NewRxForm()
        return render(request, 'refill/new_rx.html', {'info':info, 'form':form})



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
    return render(request, 'refill/refill.html')

def refill_form(request):
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

            pdf = render_to_pdf('report/refill-report.html', contect)
            return HttpResponse(pdf, content_type='application/pdf')
            return render(request, 'refill/refill_submited.html', {'refill':refill})
        return render(request, 'refill/refill_form.html', {'info': info, 'form': form})
    else:
        form = RefillForm()
        return render(request, 'refill/refill_form.html', {'info':info, 'form':form})



def one_click_refill(request):
    order=NewRx.objects.filter(info__user=request.user).filter(verified=True)
    return render(request, 'one_click_refill/one_click_refill.html', {'order':order})

def one_click_refill_submit(request,pk):
    if request.method=='GET':
        info = UserInfo.objects.filter(user=request.user)
        rx=get_object_or_404(NewRx,pk=pk)
        current_user=request.user
        if not current_user==rx.info.user:
            messages.info(request,'you are not allow here')
            return render(request, 'user_profile/user-message.html')
        else:
            if rx.verified!=True:
                messages.info(request,'this order is not verified yet')
                return render(request, 'user_profile/user-message.html')
            return render(request, 'one_click_refill/one_click_refill_submit.html', {'rx':rx, 'info':info})

    else:
        order=get_object_or_404(NewRx,pk=pk)
        drug=order.drug_set.all().count()
        order.pk=None
        order.info=UserInfo.objects.get(pk=request.POST['info'])
        order.refill=True
        order.save()
        for i in range(drug):
            if not request.POST['drug_pk{}'.format(i + 1)]=='':
                drug=Drug.objects.get(pk=request.POST['drug_pk{}'.format(i + 1)])
                drug.pk=None
                drug.med=order
                drug.save()
        messages.info(request, 'you refill order successfully submited')
        return render(request, 'user_profile/user-message.html')
