from django.conf.urls import url
from . import views

app_name= 'refill'
urlpatterns= [
    #url(r'^create/$', views.order_create, name='order_create'),
    url(r'^$', views.refill_info, name='refill-info'),

    # report html
    url(r'^report/$', views.report, name='report'),
]