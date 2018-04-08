from django.contrib import admin
from .models import Refill, Drug,NewRx
from django.forms.models import ModelForm
from user_profile.models import User, UserInfo


class AlwaysChangedModelForm(ModelForm):
    def has_changed(self):
        return True

class DrugInline(admin.TabularInline):
    extra = 0
    form = AlwaysChangedModelForm
    model = Drug
    raw_id_fields = ['med']


class DrugAdmin(admin.ModelAdmin):
    list_display = [ 'created','verified','paid','delivered','cansel','refill']
    list_filter = ['paid', 'verified', 'updated','refill']
    inlines = [DrugInline]

admin.site.register(NewRx,DrugAdmin)
admin.site.register(Refill)


