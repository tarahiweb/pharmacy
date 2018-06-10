from django.conf.urls import url
from . import views

app_name= 'emergency'
urlpatterns= [
    url(r'^emergency-info/$', views.Emergency_info, name='emergency-info'),
    url(r'^emergency-as-guest/$', views.Emergency_as_qeust_view, name='emergency-as-guest'),
    url(r'^report/emergency-as-guest/$', views.report_emergency_asguest, name='emergency-report'),

]