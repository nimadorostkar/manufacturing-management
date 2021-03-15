from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from treebeard.mp_tree import MP_Node



#------------------------------------------------------------------------------
class Station(models.Model):
    CHOICES = ( ('M','Material'), ('S','Station'), ('P','Product') )
    position=models.CharField(max_length=1,choices=CHOICES,verbose_name = "موقعیت")
    name=models.CharField(max_length=400,verbose_name = "نام")
    description=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات")
    location=models.CharField(max_length=400,verbose_name = "location")
    input=models.ForeignKey('Station',on_delete=models.CASCADE,blank=True,verbose_name = "ورودی")

    class Meta:
        verbose_name = "ایستگاه"
        verbose_name_plural = " ایستگاه ها"

    def __str__(self):
        return self.name




#------------------------------------------------------------------------------
class MyNode(MP_Node):
    place = models.OneToOneField(Station,on_delete=models.CASCADE,primary_key=True,verbose_name = "مشخصات")
    node_order_by = ['place']

    def __str__(self):
        return self.place
