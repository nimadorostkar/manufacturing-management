from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from treenode.admin import TreeNodeModelAdmin
from treenode.forms import TreeNodeForm
from .models import Category

admin.site.register(LogEntry)
admin.site.site_header= "  پنل مدیریت  "
admin.site.site_title= "Tavankar"




class CategoryAdmin(TreeNodeModelAdmin):

    # set the changelist display mode: 'accordion', 'breadcrumbs' or 'indentation' (default)
    # when changelist results are filtered by a querystring,
    # 'breadcrumbs' mode will be used (to preserve data display integrity)
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_BREADCRUMBS
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_INDENTATION

    # use TreeNodeForm to automatically exclude invalid parent choices
    form = TreeNodeForm

admin.site.register(Category, CategoryAdmin)













#------------------------------------------------------------------------------


#class ProductAdmin(admin.ModelAdmin):
#	list_display = ('name','description')
#class MaterialAdmin(admin.ModelAdmin):
#	list_display = ('name','description')
#class StationAdmin(admin.ModelAdmin):
#	list_display = ('name','description')
#class RelationAdmin(admin.ModelAdmin):
#	list_display = ('name','description')


#admin.site.register(models.Product,ProductAdmin)
#admin.site.register(models.Material,MaterialAdmin)
#admin.site.register(models.Station,StationAdmin)
#admin.site.register(models.Relation,RelationAdmin)
