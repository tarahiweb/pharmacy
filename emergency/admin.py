from django.contrib import admin

from .models import Emergency_Med,Drug
from user_profile.models import User, UserInfo

#class EmergencyAdmin(admin.ModelAdmin):
 #    list_display = ['created', 'userinfo_address','userinfo_city', 'userinfo_zip']


class DrugInline(admin.TabularInline):
    model = Drug
    raw_id_fields = ['med']


class DrugAdmin(admin.ModelAdmin):
    #list_display = [ ]
    #list_filter = ['paid', 'created', 'updated']
    inlines = [DrugInline]

admin.site.register(Emergency_Med,DrugAdmin)
#admin.site.register(EmergencyAdmin)

