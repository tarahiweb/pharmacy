from django.conf.urls import url
from . import views

app_name = 'Product'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url (r'^(?P<drug_id>[0-9]+)/$', views.details, name= 'detail'),
]

