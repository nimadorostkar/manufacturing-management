from django.contrib import admin
from . import models

admin.site.site_header= "  پنل مدیریت  "
admin.site.site_title= "Tavankar"



class ProductAdmin(admin.ModelAdmin):
	list_display = ('id','name','title')


admin.site.register(models.Product,ProductAdmin)
