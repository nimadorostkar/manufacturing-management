from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry

from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from app.models import Node



admin.site.register(LogEntry)
admin.site.site_header= "  پنل مدیریت  "
admin.site.site_title= "Tavankar"





#------------------------------------------------------------------------------
class StationAdmin(admin.ModelAdmin):
	list_display = ('name','description')

admin.site.register(models.Station,StationAdmin)




#------------------------------------------------------------------------------
class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20   # specify pixel amount for this ModelAdmin only
    #mptt_indent_field = "some_node_field"


admin.site.register(Node,DraggableMPTTAdmin,
    list_display=('tree_actions','indented_title',),
    list_display_links=('indented_title',),
	)
