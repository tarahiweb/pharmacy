from django.contrib import admin
from .models import Order, OrderItem
from user_profile.models import UserInfo

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['drug']

class OrderAdmin(admin.ModelAdmin):
    list_display = [ 'get_info','created', 'verified', ]
    # fields = ['paid', 'info.email']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


    def get_info(self,obj):
        return obj.info.user.email
    get_info.short_description = 'address'
    get_info.admin_order_field = 'info__address'

admin.site.register(Order,OrderAdmin)
