from django import forms
from .models import NewRx
from django.utils.translation import ugettext_lazy as _

class NewRxForm(forms.ModelForm):
    class Meta:
         model = NewRx
         fields = ['first_name','last_name','verify_optin','Dr_Phone_number', 'Dr_name', 'Dr_adrress','last_pharmacy', 'last_pharmacy_adrress',
              'prescription','more_refill', 'more_refill_number', ]

    def clean(self):
        cleaned_data = super().clean()
        verify_option = cleaned_data.get("verify_optin")

        if verify_option=='d':
            if cleaned_data.get("Dr_adrress")=='' or cleaned_data.get("Dr_name")=='' or cleaned_data.get("Dr_Phone_number")=='':
                raise forms.ValidationError(
                 "dr info required "
                )
        elif verify_option=='p':
            if cleaned_data.get("last_pharmacy") == '' or cleaned_data.get("last_pharmacy_adrress") == '' :
                raise forms.ValidationError(
                    "last pharmacy info required "
                )
        elif verify_option=='pr':
            if cleaned_data.get("prescription")==None:
                raise forms.ValidationError(
                    "upload the prescription "
                )
