from django.contrib import admin

from .models import Refill
from user_profile.models import User, UserInfo

class REfillAdmin(admin.ModelAdmin):
    list_display = ['created', 'userinfo_address','userinfo_city', 'userinfo_zip']


admin.site.register(Refill, REfillAdmin)

