from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey







#------------------------------------------------------------------------------
class Station(models.Model):
    CHOICES = ( ('M','Material'), ('S','Station'), ('P','Product') )
    position=models.CharField(max_length=1,choices=CHOICES,verbose_name = "موقعیت")
    name=models.CharField(max_length=400,verbose_name = "نام")
    description=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات")
    location=models.CharField(max_length=400,verbose_name = "location")
    input=models.ManyToManyField('self',blank=True,verbose_name = "ورودی")

    class Meta:
        verbose_name = "ایستگاه"
        verbose_name_plural = " ایستگاه ها"

    def __str__(self):
        return self.name


#------------------------------------------------------------------------------
class Node(MPTTModel):
    name = models.ForeignKey(Station, on_delete=models.CASCADE,verbose_name = "نام")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',verbose_name = "والد")
    #escription=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات")
    #q = models.CharField(max_length=25)


    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name
