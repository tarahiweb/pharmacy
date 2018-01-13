
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.conf import settings
from .form import UserForm,LoginForm,UserInfoForm, QuestionForm, AnswerForm
from django.contrib.auth import login as auth_login
from django.views.generic import View
from django import forms
from django.http import HttpResponse
from .models import Question, Answer


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

def user_info(request):
    form=UserInfoForm(data=request.POST)
    if form.is_valid():
        post=form.save(commit=False)
        post.user=request.user
        post.save()
        return redirect(request.GET['next'])
    else:
        return redirect(request.GET['next'])




def consulting_detail(request):
    questions = Question.objects.filter()
    return render(request, 'consulting/consulting.html', {'question': questions})


def Add_Question(request):
    if request.method=="POST":
        # age question parrent dashte bashe be onvane child question save mishe
        if request.POST['parrent']:
            if request.user.is_authenticated:
                form=AnswerForm(request.POST)
                if form.is_valid():
                    post=form.save(commit=False)
                    parrent=Question.objects.get(pk=request.POST['parrent'])
                    post.parrent=parrent
                    post.user=request.user
                    post.save()
                else:
                    return HttpResponse(form.errors)
        else:
            form=QuestionForm(request.POST)
            if form.is_valid():
                post=form.save(commit=False)
                if request.user.is_authenticated:
                    post.user=request.user
                post.save()
            else:
                return HttpResponse(form.errors)
        return redirect(request.POST['redirect'])
    else:
        return HttpResponse('get')

