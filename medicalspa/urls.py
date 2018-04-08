from django.conf.urls import url
from . import views

app_name = 'compound-info'
urlpatterns = [
    #url(r'^$', views.index, name = 'index'),
    #url (r'^component/(?P<drug_slug>[-\w]+)/$', views.details, name= 'detail'),
    url(r'^$', views.compound_info,name='compound-info'),
    # comment url
    #url(r'^comment/create-comment/', views.Add_comment, name='add-comment'),
    #compound info

]


