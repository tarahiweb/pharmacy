from django.contrib import admin

from .models import Emergency_Med,Drug, Emergency_as_guest, Drug_emergency_drug
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


class Drug_emeg_Inline(admin.TabularInline):
    model = Drug_emergency_drug
    raw_id_fields = ['med']


class Drug_emeg_Admin(admin.ModelAdmin):
    #list_display = [ ]
    #list_filter = ['paid', 'created', 'updated']
    inlines = [Drug_emeg_Inline]
admin.site.register(Emergency_as_guest, Drug_emeg_Admin)
#admin.site.register(EmergencyAdmin)

