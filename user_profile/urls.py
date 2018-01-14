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
    url(r'^consulting/add-question', views.Add_Question, name='add-question'),

    #profile
    url(r'^update-profile/', views.update_profile, name='update-profile'),
    url(r'^send_update_profile/', views.send_update_profile, name='send-update-profile'),
    url(r'^profile/', views.profile, name='profile'),
]

