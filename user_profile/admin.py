from django.contrib import admin
from .models import User,UserInfo,Question,Answer




class UserInfoInline(admin.TabularInline):
    model = UserInfo
    raw_id_fields = ['user']
class UserAdmin(admin.ModelAdmin):
    #list_display = [ ]
    #list_filter = ['paid', 'created', 'updated']
    inlines = [UserInfoInline]

class QuestionInline(admin.TabularInline):
    model = Answer
    raw_id_fields = ['parrent']
class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(User, UserAdmin)
admin.site.register(Question,QuestionAdmin)

#admin.site.register(UserProfile)
