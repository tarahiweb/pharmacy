from django.shortcuts import render, redirect
from user_profile.models import UserInfo, User
from .models import Emergency_Med,Drug, Emergency_as_guest, Drug_emergency_drug
from .forms import Emergency_MedCreateForm
from django.http import HttpResponse
from . import forms
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from pharmacy.report import render_to_pdf
from pharmacy.twilio import send_fax


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




def Emergency_as_qeust_view(request):
    #info=UserInfo.objects.filter(user=request.user)
    #user= User.objects.filter(pk=request.user.id)
    if request.method=='POST':
        form = forms.Emergency_as_guest_Form(request.POST)
        if form.is_valid():
            emergency_guest = form.save(commit=False)
            emergency_guest.save()
            for i in range(int(request.POST['drug_num'])):
                drug = Drug_emergency_drug.objects.create(drug_name=request.POST['drug_name_{}'.format(i + 1)],
                                           drug_dose=request.POST['drug_dose_{}'.format(i + 1)], med=emergency_guest)

            drugs = Drug_emergency_drug.objects.filter(med=emergency_guest)
            contect = {
                'emergency_guest': emergency_guest,
                'drug': drugs,
            }
            # email

            message = 'Your order is successfully submited, we will notify you as soon as we verify it'
            msg_html = render_to_string('email/one_text.html',
                                        {'text': message})
            send_mail(message, message,
                      settings.DEFAULT_FROM_EMAIL, [emergency_guest.Email], fail_silently=False, html_message=msg_html),

            send_fax('https://www.tysonspharmacy.us/emergency/report/emergency-as-guest/')
            # return HttpResponse(pdf, content_type='application/pdf')
            return render(request, 'refill/refill_submited.html', {'refill':emergency_guest})
        return render(request, 'emergency/emergency_as_guest.html', {'form': form})
        #return HttpResponse(form.errors)
    else:
        form = forms.Emergency_as_guest_Form()
        return render(request, 'emergency/emergency_as_guest.html', {'form':form})

def report_emergency_asguest(request):
    #info = UserInfo.objects.filter(user=request.user)
    order=Emergency_as_guest.objects.first()
    drug= Drug_emergency_drug.objects.filter(med=order)
    pdf = render_to_pdf('report/emergency-report.html', {'refill':order, "drug":drug})
    return HttpResponse(pdf, content_type='application/pdf')