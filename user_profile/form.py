
from .models import User,UserInfo, Question, Answer
from django import  forms
from django.contrib.auth.forms import AuthenticationForm


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("this email used before")
        return data

    # def
    class Meta:
        model=User
        fields=['first_name','last_name','email','password']

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        password_field = self.fields['password']
        username_field = self.fields['username']

        username_field.widget.attrs = {'class': 'inputA'}
        username_field.label = 'email'

        password_field.widget.attrs = {'class': 'inputA'}
        password_field.label = 'password'

class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=['address','zip','city']



class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields = ['body']

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields = ['body']

