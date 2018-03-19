from django.conf.urls import url
from . import views

app_name= 'refill'
urlpatterns= [
    #url(r'^create/$', views.order_create, name='order_create'),
    url(r'^new-rx/$', views.new_rx, name='new-rx'),
    url(r'^new-rx/checkout/(?P<pk>[0-9]+)/$', views.NewRx_checkout, name='new-rx-checkout'),
    url(r'^new-rx/checkout-payment/$', views.NewRx_CheckoutView.as_view(), name='newrx-checkoutview'),
    url(r'^new-rx/checkout-successful/$', views.Checkout_Successfull, name='new-rx-checkout-successful'),
    # report html
    url(r'^report/$', views.report, name='report'),

    # ajax
    url(r'^ajax/$', views.ajax, name='ajax'),
    url(r'^refill/$', views.refill_form, name='refill-form'),


    # one click refill
    url(r'^$', views.refill_objects_list, name='refill'),
    url(r'^easy-refill/(?P<pk>[0-9]+)/$', views.refill_submit, name='refill-submit'),


]