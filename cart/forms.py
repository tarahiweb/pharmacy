from django import forms

drug_quantity_choices = [(i, str(i)) for i in range(1, 21)]

class CartADDDrugForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=drug_quantity_choices, coerce=int)
    update= forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
