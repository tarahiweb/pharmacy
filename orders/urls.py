
from django.conf.urls import url
from . import views

app_name='order'
urlpatterns= [
    #url(r'^create/$', views.order_create, name='order_create'),
    url(r'^order-info/$', views.order_info, name='order_info'),
    url(r'^checkout/(?P<pk>[0-9]+)$', views.CheckoutView.as_view(), name='checkout'),
    url(r'^checkout-successful/$', views.Checkout_Successfull , name='checkout-successful'),
]