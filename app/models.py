from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from mapbox_location_field.models import LocationField






#------------------------------------------------------------------------------
class Station(models.Model):
    CHOICES = ( ('M','Material'), ('R','Repository'), ('T','Transfer'), ('S','Station') )
    position=models.CharField(max_length=1,choices=CHOICES,verbose_name = "ایستگاه")
    name=models.CharField(max_length=400,verbose_name = "نام")
    description=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات")
    input=models.ForeignKey('self',on_delete=models.CASCADE,verbose_name = "ورودی")
    city=models.CharField(max_length=70)
    location = LocationField(map_attrs={"center": [0,0], "marker_color": "blue"})

    class Meta:
        verbose_name = "ایستگاه"
        verbose_name_plural = " ایستگاه ها"

    def __str__(self):
        return self.name





#------------------------------------------------------------------------------
class Product(models.Model):
    name=models.CharField(max_length=400,verbose_name = "نام")
    description=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name




#------------------------------------------------------------------------------
# MPTT Model -->  https://django-mptt.readthedocs.io/en/latest/index.html
class Tree(MPTTModel):
    name = models.ForeignKey(Station, on_delete=models.CASCADE,verbose_name = "نام")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',verbose_name = "والد")
    relatedProduct=models.OneToOneField(Product,on_delete=models.CASCADE,primary_key=True,verbose_name = "محصول مرتبط")
    quantity = models.IntegerField(verbose_name = "ضریب مصرف")

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "درخت محصول"
        verbose_name_plural = "درخت محصولات"

    def __str__(self):
        return str(self.name)
