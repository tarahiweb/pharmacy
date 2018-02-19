from django.conf.urls import url
from . import views

app_name= 'refill'
urlpatterns= [
    #url(r'^create/$', views.order_create, name='order_create'),
    url(r'^new-rx/$', views.new_rx, name='new-rx'),

    # report html
    url(r'^report/$', views.report, name='report'),

    # ajax
    url(r'^ajax/$', views.ajax, name='ajax'),

    url(r'^refill/$', views.refill_form, name='refill-form'),
    url(r'^$', views.refill, name='refill'),

    # one click refill
    url(r'^one-click-refill/$', views.one_click_refill, name='one-click-refill'),
    url(r'^one-click-refill/(?P<pk>[0-9]+)/$', views.one_click_refill_submit, name='one-click-refill-submit'),


]