from django import forms
from .models import NewRx, Refill,NewRxAsQeust


class DateInput(forms.DateInput):
    input_type = 'date'


class NewRxForm(forms.ModelForm):
    class Meta:
         model = NewRx
         fields = ['first_name','last_name','Date_of_Birth', 'dr_phone_number', 'Dr_name', 'Dr_adrress','last_pharmacy', 'last_pharmacy_adrress',
              'prescription','more_refill', 'more_refill_number',]

         widgets = {
            'Date_of_Birth': DateInput(),
         }

    def clean(self):
        cleaned_data = super().clean()
        verify_option = cleaned_data.get("verify_optin")
        if cleaned_data.get("Dr_adrress") == '' or cleaned_data.get("Dr_name") == '' or cleaned_data.get("dr_phone_number") == '':
            doctor=False
        else:
            doctor=True
        if cleaned_data.get("last_pharmacy") == '' or cleaned_data.get("last_pharmacy_adrress") == '':
            pharmacy=False
        else:
            pharmacy=True

        if cleaned_data.get("prescription") == None:
            prescription=False
        else:
            prescription=True
        if  doctor==False and pharmacy==False and prescription==False:
            raise forms.ValidationError(
                "at least one of the varifying option is require"
            )




class RefillForm(forms.ModelForm):
    class Meta:
         model = Refill
         fields = ['first_name','last_name','Email',"Phone_number","RX_number"]
         widgets = {
            'Date_of_Birth': DateInput(),
         }





class NewRx_CheckoutForm(forms.Form):
    payment_method_nonce = forms.CharField(
        max_length=1000,
        widget=forms.widgets.HiddenInput,
        required=False,  # In the end it's a required field, but I wanted to provide a custom exception message
    )
    #amount= forms.DecimalField(max_digits=10, decimal_places=2,)



    def clean(self):
        self.cleaned_data = super(NewRx_CheckoutForm, self).clean()
        # Braintree nonce is missing
        if not self.cleaned_data.get('payment_method_nonce'):
            raise forms.ValidationError(_(
                'We couldn\'t verify your payment. Please try again.'))
        return self.cleaned_data



class NewRxAsGeustForm(forms.ModelForm):
    class Meta:
         model = NewRxAsQeust
         fields = ['first_name','last_name','email','phone_number', 'dr_phone_number', 'Dr_name', 'Dr_adrress','last_pharmacy', 'last_pharmacy_adrress',
              'prescription']

         widgets = {
            'Date_of_Birth': DateInput(),
         }

    def clean(self):
        cleaned_data = super().clean()
        verify_option = cleaned_data.get("verify_optin")
        if cleaned_data.get("Dr_adrress") == '' or cleaned_data.get("Dr_name") == '' or cleaned_data.get("dr_phone_number") == '':
            doctor=False
        else:
            doctor=True
        if cleaned_data.get("last_pharmacy") == '' or cleaned_data.get("last_pharmacy_adrress") == '':
            pharmacy=False
        else:
            pharmacy=True

        if cleaned_data.get("prescription") == None:
            prescription=False
        else:
            prescription=True
        if  doctor==False and pharmacy==False and prescription==False:
            raise forms.ValidationError(
                "At least one of the varifying option is require"
            )

