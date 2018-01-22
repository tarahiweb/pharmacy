from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login,logout
from django.conf import settings
from .form import UserForm,LoginForm,UserInfoForm, QuestionForm, AnswerForm
from django.contrib.auth import login as auth_login
from django.views.generic import View
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Answer, User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy




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

@login_required(login_url='user_profile:login')
def consulting_detail(request):
    if request.method=='GET':
        questions = Question.objects.all()
        return render(request, 'consulting/consulting.html', {'question': questions})
    else:
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
            return HttpResponse('ok')
        else:
            form=QuestionForm(request.POST)
            if form.is_valid():
                post=form.save(commit=False)
                if request.user.is_authenticated:
                    post.user=request.user
                post.save()
            else:
                return HttpResponse(form.errors)
        return HttpResponse('ok')



@login_required(login_url='user_profile:login')
def profile(request):
        if request.user.is_authenticated:
            user= User.objects.get(id=request.user.id)
            return render_to_response('user_profile/profile.html', {'user': user})


class EditView(LoginRequiredMixin, UpdateView):
    login_url = 'user_profile:login'
    model = User
    template_name = 'user_profile/form.html'
    fields = ['first_name', 'last_name', 'email']
    def get_object(self, queryset=None):
        return self.request.user

    success_url = reverse_lazy('home')

