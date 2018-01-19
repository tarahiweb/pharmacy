from django.contrib import admin

from .models import Emergency_Med
from user_profile.models import User, UserInfo

class EmergencyAdmin(admin.ModelAdmin):
    list_display = ['created', 'userinfo_address','userinfo_city', 'userinfo_zip']


admin.site.register(Emergency_Med, EmergencyAdmin)
