from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin
from .views import Home, Privacy, Terms,test,contact_us
from django.contrib.auth.views import password_reset,password_reset_done,password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home,name='home'),
    url(r'^privacy-and-policy$',Privacy , name='privacy'),
    url(r'^Terms-and-conditions$', Terms, name='terms'),
    url(r'^compound-info/', include('medicalspa.urls', namespace='compound-info')),
    url(r'^emergency/', include('emergency.urls', namespace='emergency')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^product/', include('Product.urls')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^refill/', include('refill.urls', namespace='refill')),
    url(r'^user/', include('user_profile.urls')),

    # password
    url(r'password/$', password_reset,{'template_name': 'password_reset/password_reset.html'}, name='reset_password'),
    url(r'password/done/$', password_reset_done,{'template_name': 'password_reset/password_reset_done.html'}, name='password_reset_done'),
    url(r'password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm,{'template_name': 'password_reset/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'password/complete/$', password_reset_complete,{'template_name': 'password_reset/password_reset_complete.html'},  name='password_reset_complete'),

    # test
    url(r'^test/',test ),

    # other
    url(r'^contact-us/', contact_us,name='contact-us'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)