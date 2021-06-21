from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from mapbox_location_field.admin import MapAdmin
from .models import Profile, Tree, Process, Ticket, Order, Supplier
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportMixin




admin.site.site_header= "  پنل مدیریت  "
admin.site.site_title= "Tavankar"

admin.site.register(LogEntry)





#------------------------------------------------------------------------------
class SupplierAdmin(ImportExportModelAdmin):
    list_display = ('name','phone_number','website')

admin.site.register(models.Supplier, SupplierAdmin)



#------------------------------------------------------------------------------
class TicketAdmin(ImportExportModelAdmin):
    list_display = ('user','to','title','created_on')
    list_filter = ("user", "to", "created_on")

admin.site.register(models.Ticket, TicketAdmin)



#------------------------------------------------------------------------------
class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('user_name','phone','address')

admin.site.register(models.Profile, ProfileAdmin)



#------------------------------------------------------------------------------
class ProcessAdmin(ImportExportModelAdmin):
    list_display = ('name','manager','short_description','inventory','position')
    list_filter = ("manager", "position")

admin.site.register(models.Process, ProcessAdmin)



#------------------------------------------------------------------------------
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name','short_description','code','image_tag')

admin.site.register(models.Product, ProductAdmin)


#------------------------------------------------------------------------------
 #https://django-mptt.readthedocs.io/en/latest/admin.html#mptt-admin-draggablempttadmin
class TreeMPTTModelAdmin(ImportExportMixin, MPTTModelAdmin):
    mptt_level_indent = 15   # specify pixel amount for this ModelAdmin only
    #mptt_indent_field = "some_node_field"

admin.site.register(Tree, DraggableMPTTAdmin,
    list_display=('tree_actions','indented_title','position'),
    #list_editable = ('quantity'),
    list_display_links=('indented_title',),)



#------------------------------------------------------------------------------
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('product','code','circulation')
    list_filter = ("product", "circulation")

admin.site.register(models.Order, OrderAdmin)



#------------------------------------------------------------------------------
class Process_OrderAdmin(ImportExportModelAdmin):
    list_display = ('process','code','circulation')
    list_filter = ("process", "circulation")

admin.site.register(models.Process_Order, Process_OrderAdmin)













#-------------------------------------------------------- by Nima Dorostkar ---
