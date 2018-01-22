from django.conf.urls import url
from . import views

app_name = 'medicalspa'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url (r'^(?P<drug_slug>[-\w]+)/$', views.details, name= 'detail'),

    # comment url
    url(r'^comment/create-comment/', views.Add_comment, name='add-comment'),
    #compound info

]


