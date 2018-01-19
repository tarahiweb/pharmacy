from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^order-info/$', views.order_info, name='order_info'),
]