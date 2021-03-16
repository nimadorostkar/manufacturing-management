from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry






admin.site.register(LogEntry)
admin.site.site_header= "  پنل مدیریت  "
admin.site.site_title= "Tavankar"





class StationAdmin(admin.ModelAdmin):
	list_display = ('name','description')



admin.site.register(models.Station,StationAdmin)
