from django import forms

from django import forms
from .models import Compound

class CompoundCreateForm(forms.ModelForm):
    class Meta:
         model = Compound
         fields = ["First_name", 'Last_name']


class Coumpound_not_logged_in_form(forms.ModelForm):
    class Meta:
        model =Compound
        fields= ["First_name", 'Last_name', 'Phone_number','Email_address','State','City','Zip']