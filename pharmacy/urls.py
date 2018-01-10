from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin
from .views import Home
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home,name='home'),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^product/', include('Product.urls')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^user/', include('user_profile.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)