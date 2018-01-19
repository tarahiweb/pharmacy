from django.conf.urls import url
from . import views

app_name= 'emergency'
urlpatterns= [
    url(r'^emergency-info/$', views.Emergency_info, name='emergency-info'),
]