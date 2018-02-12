from django.conf.urls import url
from . import views

app_name= 'refill'
urlpatterns= [
    #url(r'^create/$', views.order_create, name='order_create'),
    url(r'^NewRx/$', views.new_rx, name='new-rx'),

    # report html
    url(r'^report/$', views.report, name='report'),

    # ajax
    url(r'^ajax/$', views.ajax, name='ajax'),

    url(r'^Refill/$', views.refill, name='refill'),



]