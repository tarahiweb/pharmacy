from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    pass
    # class Meta:
    #     model = Order
    #     fields = ['first_name', 'last_name', 'email', 'address', 'zip', 'city']