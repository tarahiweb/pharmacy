from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.conf import settings
from .form import UserForm,LoginForm,UserInfoForm, QuestionForm, AnswerForm,PhoneForm
from django.contrib.auth import login as auth_login
from django.views.generic import View
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Answer, User,UserInfo
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from emergency.models import Emergency_Med
from refill.models import NewRx,Drug
from orders.models import Order
from refill.views import new_rx
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='user_profile:login')
def profile(request):
    current_user= request.user

    # emergency
    eme_all=Emergency_Med.objects.filter(info__user=current_user)
    eme_verified=eme_all.filter(verified=True)

    # refill
    refill_all=NewRx.objects.filter(info__user=current_user)
    refill_verfied=refill_all.filter(verified=True)

    # free product order
    free_product_all=Order.objects.filter(info__user=current_user)
    free_product_verified=free_product_all.filter(verified=True)
    context={
        'user': current_user,
        # emergency
        'eme_all': eme_all,
        'eme_verified':eme_verified,
        # refil
        'refill_all':refill_all,
        'refill_verfied':refill_verfied,
        # free product
        'free_all':free_product_all,
        'free_verified':free_product_verified
    }
    return render_to_response('user_profile/profile.html', context)


class UserFormView(View):
    form_class = UserForm
    template_name = 'user_profile/register_form.html'
    #
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('home')
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            email = form.cleaned_data['email']
            user.username=email
            user.save()
            karbar = authenticate(username=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    try:
                        return redirect(request.GET['next'])
                    except:
                        return redirect('home')
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'user_profile/login.html'
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('home')
        form = LoginForm()
        return render(request, self.template_name, {
            'form': form
        })

    def post(self, request):
        if request.user.is_authenticated():
            return redirect('user_profile:index')

        form = LoginForm(data=request.POST)
        if form.is_valid():

            user = form.get_user()
            auth_login(request, user)
            try:
                redirect_to=request.GET['next']
                return redirect(request.GET['next'])
            except:
                pass

            return redirect('home')

        return render(request, self.template_name, {
            'form': form
        })

def Logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='user_profile:login')
def user_info(request):
    form=UserInfoForm(data=request.POST)
    if form.is_valid():
        post=form.save(commit=False)
        post.user=request.user
        post.save()
        return redirect(request.GET['next'])
    else:
        return HttpResponse(form.errors)
        return redirect(request.GET['next'])



class EditView(LoginRequiredMixin, UpdateView):
    login_url = 'user_profile:login'
    model = User
    template_name = 'user_profile/form.html'
    fields = ['first_name', 'last_name', 'email']
    def get_object(self, queryset=None):
        return self.request.user

    success_url = reverse_lazy('user_profile:profile')

def RefillList(request):
        current_user= request.user
        refilllist = NewRx.objects.filter(info__user=current_user)
        refil_num= len(refilllist)
        return render(request, 'user_profile/profile_refill_orders.html', {'refilllist':refilllist, 'refil_num':refil_num})

def Emergencylist(request):
    current_user = request.user
    emergencylist= Emergency_Med.objects.filter(info__user=current_user)
    emergency_len= len(emergencylist)
    return render (request, 'user_profile/profile_emergency-orders.html', {'emergencylist': emergencylist, 'emergency_len':emergency_len})



def Freeorderlist(request):
    current_user=request.user
    freeorderlist= Order.objects.filter(info__user=current_user)
    freeproducts_len = len(freeorderlist)
    return render(request, 'user_profile/profile_freeproducts-orders.html', {'freeorderlist':freeorderlist, 'freeproducts_len':freeproducts_len})



@login_required(login_url='user_profile:login')
def consulting_ask(request):
    if request.method=='GET':
        return render(request, 'consulting/consulting-ask.html')
    else:
        form = QuestionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('user_profile:consulting-show', pk=post.pk)
        else:
            return HttpResponse(form.errors)


def consulting(request):
    question=Question.objects.filter(user=request.user)
    return render(request,'consulting/consulting.html',{'question':question})

def consulting_show(request,pk):
    if request.method == 'GET':
        question=Question.objects.filter(user=request.user)
        question_show=Question.objects.get(pk=pk)
        answer=Answer.objects.filter(parrent=question_show)
        return render(request, 'consulting/consulting-show.html', {'question': question,'question_show':question_show,'answer':answer})
    else:
        form = AnswerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            parrent = Question.objects.get(pk=pk)
            post.parrent = parrent
            post.user = request.user
            post.save()
            return redirect('user_profile:consulting-show', pk=pk)
        else:
            return HttpResponse(form.errors)

@csrf_exempt
def add_phone(request):
    if request.method == 'POST':
        form=PhoneForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            user=request.user
            user.phone_number=post.phone_number
            user.save()
            res='okkk'
        res=form.errors
        result={
            'result':res
        }
        return JsonResponse(result)
    else:
        form = PhoneForm({'add_phone':request.user.phone_number})
        return render(request,'user_profile/form.html',{'form':form})

