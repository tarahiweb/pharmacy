from django import forms
from .models import Refill

class RefillCreateForm(forms.ModelForm):
    class Meta:
         model = Refill
         fields = ['Dr_Phone_number', 'Dr_name', 'Dr_adrress', 'last_pharmacy', 'last_pharmacy_adrress', 'drug_name', 'drug_dose', 'prescription', 'more_refill']