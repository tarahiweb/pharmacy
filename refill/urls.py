from django.conf.urls import url
from . import views

app_name= 'refill'
urlpatterns= [
    #url(r'^create/$', views.order_create, name='order_create'),
    url(r'^refill-info/$', views.refill_info, name='refill-info'),
]