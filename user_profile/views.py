
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.conf import settings
from .form import UserForm,LoginForm
from django.contrib.auth import login as auth_login
from django.views.generic import View


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