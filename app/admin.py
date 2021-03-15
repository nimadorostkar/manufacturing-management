from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from .models import Product
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory





admin.site.register(LogEntry)
admin.site.site_header= "  پنل مدیریت  "
admin.site.site_title= "Tavankar"




class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Product)
class StationAdmin(admin.ModelAdmin):
	list_display = ('name','description')


admin.site.register(Product, MyAdmin)
admin.site.register(models.Station,StationAdmin)
