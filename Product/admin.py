from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget

class DrugAdmin(admin.ModelAdmin):
    list_display = ( 'drug_name', 'drug_company')
    search_fields = ('drug_name', 'drug_company')
    prepopulated_fields = {'slug': ('drug_name',)}
    formfield_overrides = {
            models.TextField: {'widget': AdminPagedownWidget},
        }

# Register your models here.
from .models import Drug,Comment
admin.site.register(Drug,DrugAdmin)
admin.site.register(Comment)

