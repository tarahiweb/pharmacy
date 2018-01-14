from django.contrib import admin

# Register your models here.
from .models import User,UserInfo,Question
class UserInfoInline(admin.TabularInline):
    model = UserInfo
    raw_id_fields = ['user']


class UserAdmin(admin.ModelAdmin):
    #list_display = [ ]
    #list_filter = ['paid', 'created', 'updated']
    inlines = [UserInfoInline]

admin.site.register(User, UserAdmin)
admin.site.register(Question)
#admin.site.register(UserProfile)