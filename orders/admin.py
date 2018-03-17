from django.contrib import admin
from django.forms import ModelForm

from .models import Order, OrderItem
from user_profile.models import User, UserInfo


class AlwaysChangedModelForm(ModelForm):
    def has_changed(self):
        return True

class OrderItemInline(admin.TabularInline):
    extra = 0
    form = AlwaysChangedModelForm
    model = OrderItem
    raw_id_fields = ['drug']

class OrderAdmin(admin.ModelAdmin):
    list_display = [ 'get_info','created', 'paid','get_phone','get_email' ]
    # fields = ['paid', 'info']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

    def get_info(self,obj):
        return obj.info.address
    get_info.short_description = 'address'
    get_info.admin_order_field = 'info__address'

    def get_phone(self,obj):
        return obj.info.user.phone_number
    get_phone.short_description = 'phone number'
    get_phone.admin_order_field = 'an'

    def get_email(self,obj):
        return obj.info.user.email
    get_email.short_description = 'email'
    get_email.admin_order_field = 'info__address'

admin.site.register(Order,OrderAdmin)
