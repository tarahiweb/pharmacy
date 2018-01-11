from django.shortcuts import render, redirect
from user_profile.models import UserInfo
from .models import OrderItem,Order
from .forms import OrderCreateForm
from cart.cart import Cart
from user_profile.views import UserFormView, LoginView


def order_info(request):
    info=UserInfo.objects.filter(user=request.user)
    cart = Cart(request)
    if request.method=='POST':
        pass
    else:
        return render(request,'orders/info-chek.html',{'info':info,'cart':cart})


def order_create(request):
    cart =Cart(request)
    if request.method == 'POST' :
            info=UserInfo.objects.get(pk=request.POST['info'])
            order=Order.objects.create(info=info)
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

