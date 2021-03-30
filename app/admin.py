from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from app.models import Tree
from app.models import Station
from mapbox_location_field.admin import MapAdmin






admin.site.register(LogEntry)
admin.site.site_header= "  پنل مدیریت  "
admin.site.site_title= "Tavankar"




#------------------------------------------------------------------------------
 #https://django-mptt.readthedocs.io/en/latest/admin.html#mptt-admin-draggablempttadmin
class StationMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20   # specify pixel amount for this ModelAdmin only
    #mptt_indent_field = "some_node_field"

admin.site.register(Station,DraggableMPTTAdmin,
    list_display=('tree_actions','indented_title',),
    list_display_links=('indented_title',),
	)



#------------------------------------------------------------------------------
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','description')

admin.site.register(models.Product,ProductAdmin)




#------------------------------------------------------------------------------
 #https://django-mptt.readthedocs.io/en/latest/admin.html#mptt-admin-draggablempttadmin
class TreeMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20   # specify pixel amount for this ModelAdmin only
    #mptt_indent_field = "some_node_field"

admin.site.register(Tree,DraggableMPTTAdmin,
    list_display=('tree_actions','indented_title',),
    list_display_links=('indented_title',),
	)
