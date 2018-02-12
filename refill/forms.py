from django import forms
from .models import NewRx, Refill


class DateInput(forms.DateInput):
    input_type = 'date'


class NewRxForm(forms.ModelForm):
    class Meta:
         model = NewRx
         fields = ['first_name','last_name','Date_of_Birth', 'verify_optin','dr_phone_number', 'Dr_name', 'Dr_adrress','last_pharmacy', 'last_pharmacy_adrress',
              'prescription','more_refill', 'more_refill_number',]

         widgets = {
            'Date_of_Birth': DateInput(),
         }

    def clean(self):
        cleaned_data = super().clean()
        verify_option = cleaned_data.get("verify_optin")

        if verify_option=='d':
            if cleaned_data.get("Dr_adrress")=='' or cleaned_data.get("Dr_name")=='' or cleaned_data.get("dr_phone_number")=='':
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
        more_refill = cleaned_data.get("more_refill")
        if more_refill:
            if cleaned_data.get("more_refill_number") == '':
                raise forms.ValidationError("please specify the number of refills you need")





class RefillForm(forms.ModelForm):
    class Meta:
         model = Refill
         fields = ['first_name','last_name','Date_of_Birth','RX_number', 'more_refill', 'more_refill_number',]
         widgets = {
            'Date_of_Birth': DateInput(),
         }

    def clean(self):
        cleaned_data = super().clean()
        more_refill = cleaned_data.get("more_refill")
        if more_refill:
            if cleaned_data.get("more_refill_number") == '':
                raise forms.ValidationError("please specify the number of refills you need")
