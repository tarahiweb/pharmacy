from django.conf.urls import url
from . import views


app_name='compoundinfo'
urlpatterns = [

url(r'^$', views.compound_info, name='compound-info'),
        ]