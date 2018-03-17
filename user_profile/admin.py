from django.contrib import admin
from django.forms import ModelForm

from .models import User,UserInfo,Question,Answer
from refill.models import NewRx


class AlwaysChangedModelForm(ModelForm):
    def has_changed(self):
        return True


class UserInfoInline(admin.TabularInline):
    model = UserInfo
    raw_id_fields = ['user']


class UserAdmin(admin.ModelAdmin):
    #list_display = [ ]
    #list_filter = ['paid', 'created', 'updated']
    inlines = [UserInfoInline]

class QuestionInline(admin.TabularInline):
    extra = 0
    form = AlwaysChangedModelForm
    model = Answer
    raw_id_fields = ['parrent']
class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(User, UserAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(UserInfo)

#admin.site.register(UserProfile)
