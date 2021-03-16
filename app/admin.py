from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from myproject.myapp.models import Node







admin.site.register(LogEntry)
admin.site.site_header= "  پنل مدیریت  "
admin.site.site_title= "Tavankar"





class StationAdmin(admin.ModelAdmin):
	list_display = ('name','description')

class CustomMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20



admin.site.register(models.Station,StationAdmin)


admin.site.register(Node, CustomMPTTModelAdmin)
