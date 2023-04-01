from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import Foodsales

class FoodsalesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['OrderDate','Region','City','Category','Product','Quantity','UnitPrice']

admin.site.register(Foodsales,FoodsalesAdmin)