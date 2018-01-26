from django.conf.urls import url
from . import views

app_name = 'product'


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url (r'^(?P<category_slug>[-\w]+)/$', views.index, name='product_list_by_category'),
    url (r'^Drug/(?P<drug_slug>[-\w]+)/$', views.details, name='detail'),

    # comment url
    url(r'^comment/create-comment/', views.Add_comment, name='add-comment'),
]
