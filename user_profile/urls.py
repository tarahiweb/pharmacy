from django.conf.urls import url
from . import views
from refill.views import refill_objects_list,refill_submit
app_name = 'user_profile'

urlpatterns = [
    url(r'^register', views.UserFormView.as_view(), name = 'register'),
    url(r'^login', views.LoginView.as_view(), name = 'login'),
    url(r'^logout', views.Logout, name = 'logout'),

    # userinfo
    url(r'^create-info', views.user_info, name='create-userinfo'),
    #consulting
    url(r'^consulting/ask', views.consulting_ask, name='consulting_ask'),
    url(r'^consulting/show/(?P<pk>[0-9]+)/$', views.consulting_show, name='consulting-show'),
    url(r'^consulting/$', views.consulting, name='consulting'),
    url(r'^consulting-as-guest/$', views.consultiong_as_qeust_view, name='consulting-as-guest'),
    url(r'^report/consulting-as-guest/$', views.report_consulting_asguest, name='report-consulting-as-guest'),
    #profile
    url(r'^$', views.profile, name='profile'),
    url(r'^update', views.EditView.as_view(), name='update'),
    url(r'^changepassword', views.ChangePassword, name='password'),

    url(r'^orders', views.order, name='orders'),
    url(r'^orders', views.order, name='orders'),


    # add phone
    url(r'^add-phone', views.add_phone, name='add-phone'),

]


