from django.shortcuts import render , redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Product.models import Drug
from .cart import Cart
from .forms import CartADDDrugForm

@require_POST
def cart_add(request, drug_id):
    cart =Cart(request)
    drug = get_object_or_404(Drug, id = drug_id)
    form = CartADDDrugForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(drug = drug, quantity= cd['quantity'], update_quantity= cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, drug_id):
    cart = Cart(request)
    drug = get_object_or_404(Drug, id= drug_id)
    cart.remove(drug)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})