from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget
from .models import Drug,Comment, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)



class DrugAdmin(admin.ModelAdmin):
    list_display = ( 'drug_name', 'drug_company', 'category', 'price', 'over_the_counter')
    list_filter = ['created', 'category']
    list_editable = ['price', 'over_the_counter']
    search_fields = ('drug_name', 'drug_company')
    prepopulated_fields = {'slug': ('drug_name',)}
    formfield_overrides = {
            models.TextField: {'widget': AdminPagedownWidget},
        }



admin.site.register(Drug,DrugAdmin)
admin.site.register(Comment)


