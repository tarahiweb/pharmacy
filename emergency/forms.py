from django import forms
from .models import Emergency_Med

class Emergency_MedCreateForm(forms.ModelForm):
    class Meta:
         model = Emergency_Med
         fields = ['Dr_Phone_number', 'Dr_name', 'Dr_adrress', 'last_pharmacy', 'last_pharmacy_adrress']