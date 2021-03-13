from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse




#------------------------------------------------------------------------------
#class Station(models.Model):
#    CHOICES = ( ('M','Material'), ('S','Station'), ('P','Product') )
#    position=models.CharField(max_length=1, choices=CHOICES,verbose_name = "موقعیت")
#    name=models.CharField(max_length=400,verbose_name = "نام")
#    description=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات")
#    location=models.CharField(max_length=400,verbose_name = "location")
#    input=models.ManyToManyField('Station',blank=True,verbose_name = "ورودی")


#    class Meta:
#        verbose_name = "ایستگاه"
#        verbose_name_plural = " ایستگاه ها"

#    def __str__(self):
#        return self.name




#------------------------------------------------------------------------------
#class Product(TreeNodeModel):
    # the field used to display the model instance
    # default value 'pk'
#    treenode_display_field = 'station'

#    station = models.ForeignKey(Station,on_delete=models.CASCADE,verbose_name = "ایستگاه")

#    class Meta(TreeNodeModel.Meta):
#        verbose_name = 'محصول'
#        verbose_name_plural = 'محصول ها'
