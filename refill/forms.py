from django import forms
from .models import Refill
from django.utils.translation import ugettext_lazy as _

class RefillCreateForm(forms.ModelForm):
    class Meta:
         model = Refill
         fields = ['verify_with_DR','Dr_Phone_number', 'Dr_name', 'Dr_adrress', 'vedrify_with_Pharmacy','last_pharmacy', 'last_pharmacy_adrress',
             'verify_with_prescription', 'prescription','more_refill', 'more_refill_number', 'choose_your_shipment_method']

    def fields_required(self, fields):
        """Used for conditionally marking fields as required."""
        for field in fields:
            if not self.cleaned_data.get(field, ''):
                msg = forms.ValidationError("This field is required.")
                self.add_error(field, msg)

    def clean(self):
        dr_verification = self.cleaned_data.get('verify_with_DR')

        if dr_verification:
            self.fields_required(['Dr_name', 'Dr_Phone_number', 'Dr_adrress'])
        else:
            self.cleaned_data['Dr_name'] = ''
            self.cleaned_data['Dr_Phone_number']=''
            self.cleaned_data['Dr_adrress'] = ''


        pharmacy_verification= self.cleaned_data.get('vedrify_with_Pharmacy')
        if pharmacy_verification:
            self.fields_required(['last_pharmacy', 'last_pharmacy_adrress'])
        else:
            self.cleaned_data['last_pharmacy'] = ''
            self.cleaned_data['last_pharmacy_adrress'] = ''

        prescription_verification= self.cleaned_data.get('verify_with_prescription')
        if prescription_verification:
            self.fields_required(['prescription'])
        else:
            self.cleaned_data['prescription']=''
        return self.cleaned_data

    def method_required(self):
        if not Refill.vedrify_with_Pharmacy:
            if not Refill.verify_with_DR:
                if not Refill.verify_with_prescription:
                   msg=forms.ValidationError("at least one is required")
                   self.add_error('Dr_name' , msg)