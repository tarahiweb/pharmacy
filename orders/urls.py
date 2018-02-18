
from django.conf.urls import url
from . import views

urlpatterns= [
    #url(r'^create/$', views.order_create, name='order_create'),
    url(r'^order-info/$', views.CheckoutView.as_view(), name='order_info'),
]