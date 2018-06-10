from django.conf.urls import url
from . import views

app_name= 'refill'
urlpatterns= [
    url(r'^new-rx/$', views.new_rx, name='new-rx'),
    url(r'^new-rx/checkout/(?P<pk>[0-9]+)/$', views.NewRx_checkout, name='new-rx-checkout'),
    url(r'^new-rx/checkout-payment/$', views.NewRx_CheckoutView.as_view(), name='newrx-checkoutview'),
    url(r'^new-rx/checkout-successful/$', views.Checkout_Successfull, name='new-rx-checkout-successful'),
    # report html
    url(r'^report/NewRx/$', views.report_newRx, name='report'),
    url(r'^report/NewRx-as-guest/$', views.report_newRx_asguest, name='report-newrx'),
    url(r'^report/refill-as-guest/$', views.report_refill_asguest, name='report-refill'),
    # ajax
    url(r'^ajax/$', views.ajax, name='ajax'),

    # qeust
    url(r'^refill_as_qeust/$', views.refill_as_qeust, name='refill-as-qeust'),
    url(r'^newrx_as_qeust/$', views.newrx_as_qeust, name='newrx-as-qeust'),


    # one click refill
    url(r'^$', views.refill_objects_list, name='refill'),
    url(r'^easy-refill/(?P<pk>[0-9]+)/$', views.refill_submit, name='refill-submit'),


]