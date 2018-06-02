from django import forms
from .models import Emergency_Med, Emergency_as_guest

class DateInput(forms.DateInput):
    input_type = 'date'


class Emergency_MedCreateForm(forms.ModelForm):
    class Meta:
         model = Emergency_Med
         fields = ['Dr_Phone_number', 'Dr_name', 'Dr_adrress', 'last_pharmacy', 'last_pharmacy_adrress']




class Emergency_as_guest_Form(forms.ModelForm):
    class Meta:
         model = Emergency_as_guest
         fields = ['first_name','last_name','Date_of_Birth','Email',"Phone_number"]
         widgets = {
            'Date_of_Birth': DateInput(),
         }
