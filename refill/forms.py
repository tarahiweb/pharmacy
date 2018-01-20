from django import forms
from .models import Refill

class RefillCreateForm(forms.ModelForm):
    class Meta:
         model = Refill
         fields = ['Dr_Phone_number', 'Dr_name', 'Dr_adrress', 'last_pharmacy', 'last_pharmacy_adrress'
             , 'prescription','more_refill', 'more_refill_number', 'choose_your_shipment_method']