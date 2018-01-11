from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from user_profile.views import UserFormView, LoginView



def order_create(request):
    cart =Cart(request)
    if request.user.is_authenticated():
        if request.method == 'POST' :
                form = OrderCreateForm(request.POST)
                if form.is_valid():
                    order = form.save()
                    for item in cart :
                        OrderItem.objects.create(order= order,
                                                 drug=item['drug'],
                                                 #price=item['price'],
                                                 quantity=item['quantity'])


                        cart.clear()
                        return render(request, 'orders/created.html', {'order':order})

        else:
            form = OrderCreateForm()
            return render(request, 'orders/create.html', {'cart': cart, 'form': form} )

    else:
        return redirect('user_profile:login')