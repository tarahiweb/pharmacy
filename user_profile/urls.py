from django.conf.urls import url
from . import views

app_name = 'user_profile'

urlpatterns = [
    url(r'^register', views.UserFormView.as_view(), name = 'register'),
    url(r'^login', views.LoginView.as_view(), name = 'login'),
    url(r'^logout', views.Logout, name = 'logout'),

    # userinfo
    url(r'^create-info', views.user_info, name='create-userinfo'),
    #consulting
    url(r'^consulting/', views.consulting_detail, name='consulting_detail'),

    #profile
    url(r'^$', views.profile, name='profile'),
    url(r'^update', views.EditView.as_view(), name='update'),
    url(r'^your-orders', views.RefillList, name='your-order')



]

