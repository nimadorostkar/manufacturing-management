from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from treenode.admin import TreeNodeModelAdmin
from treenode.forms import TreeNodeForm
from .models import Product


admin.site.register(LogEntry)
admin.site.site_header= "  پنل مدیریت  "
admin.site.site_title= "Tavankar"




class StationAdmin(admin.ModelAdmin):
	list_display = ('name','description')
class ProductAdmin(TreeNodeModelAdmin):
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION
    form = TreeNodeForm


admin.site.register(models.Station,PlaceAdmin)
admin.site.register(Product, ProductAdmin)
