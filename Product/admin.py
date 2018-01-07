from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget

class DrugAdmin(admin.ModelAdmin):
    list_display = ( 'drug_name', 'drug_company')
    search_fields = ('drug_name', 'drug_company')
    formfield_overrides = {
            models.TextField: {'widget': AdminPagedownWidget},
        }

# Register your models here.
from .models import Drug
admin.site.register(Drug,DrugAdmin)

