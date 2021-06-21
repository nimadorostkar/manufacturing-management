from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from mapbox_location_field.admin import MapAdmin
from .models import Profile, Tree, Process, Ticket, Order, Supplier
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin





admin.site.site_header= " توانکار "
admin.site.site_title= "Tavankar"

admin.site.register(LogEntry)





#------------------------------------------------------------------------------
class SupplierAdmin(ImportExportModelAdmin):
    list_display = ('name', 'link')

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
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('product','code','circulation', 'get_created_jalali')
    list_filter = ("product", "circulation")

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')
    get_created_jalali.short_description = " زمان شروع "

admin.site.register(models.Order, OrderAdmin)



#------------------------------------------------------------------------------
class Process_OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('process','code','circulation', 'get_created_jalali')

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')
    get_created_jalali.short_description = " زمان شروع "

admin.site.register(models.Process_Order, Process_OrderAdmin)




#------------------------------------------------------------------------------
class NoticeAdmin(ImportExportModelAdmin):
    list_display = ('title','content','created_on')

admin.site.register(models.Notice, NoticeAdmin)










#-------------------------------------------------------- by Nima Dorostkar ---
