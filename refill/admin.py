from django.contrib import admin
from .models import Refill, Drug,NewRx,Drug_refill,NewRxAsQeust
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

class DrugForRefilInline(admin.TabularInline):
    extra = 0
    form = AlwaysChangedModelForm
    model = Drug_refill
    raw_id_fields = ['med']
class DrugForRefillAdmin(admin.ModelAdmin):
    list_display = [ 'Phone_number','first_name','last_name','Email','RX_number']
    list_filter = ['Phone_number', 'first_name','last_name','Email','RX_number']
    inlines = [DrugForRefilInline]

admin.site.register(NewRx,DrugAdmin)
admin.site.register(Refill,DrugForRefillAdmin)
admin.site.register(NewRxAsQeust)


