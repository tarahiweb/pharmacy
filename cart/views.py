from django.shortcuts import render , redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Product.models import Drug
from .cart import Cart
from .forms import CartADDDrugForm
from django.http import HttpResponse


def cart_add(request, drug_id):
    cart =Cart(request)
    drug = get_object_or_404(Drug, id = drug_id)
    form = CartADDDrugForm(request.POST)
    cart.add(drug = drug, quantity= 1, update_quantity= False)
    return redirect('cart:cart_detail')

def cart_remove(request, drug_id):
    cart = Cart(request)
    drug = get_object_or_404(Drug, id= drug_id)
    cart.remove(drug)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    drug=Drug.objects.all()
    # return HttpResponse(cart)
    return render(request, 'cart/detail.html', {'cart': cart})