
from django.conf.urls import url
from . import views

urlpatterns= [
    #url(r'^create/$', views.order_create, name='order_create'),
    url(r'^order-info/$', views.order_info, name='order_info'),
    url(r'^checkout/$', views.CheckoutView.as_view(), name='checkout'),
]