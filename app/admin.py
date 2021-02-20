from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
admin.site.register(LogEntry)


admin.site.site_header= "  پنل مدیریت  "
admin.site.site_title= "Tavankar"





class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','description')
class MaterialAdmin(admin.ModelAdmin):
	list_display = ('name','description')
class StationAdmin(admin.ModelAdmin):
	list_display = ('name','description')


admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.Material,MaterialAdmin)
admin.site.register(models.Station,StationAdmin)
