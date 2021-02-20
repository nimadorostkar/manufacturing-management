from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse



#------------------------------------------------------------------------------
class Station(models.Model):
    name=models.CharField(max_length=400,verbose_name = "نام")
    description=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات")

    class Meta:
        verbose_name = "ایستگاه"
        verbose_name_plural = "ایستگاه ها"

    def __str__(self):
        return self.name


#------------------------------------------------------------------------------
class Material(models.Model):
    name=models.CharField(max_length=400,verbose_name = "نام")
    description=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات")

    class Meta:
        verbose_name = "قطعه"
        verbose_name_plural = "قطعات"

    def __str__(self):
        return self.name



#------------------------------------------------------------------------------
class Relation(models.Model):
    name=models.CharField(max_length=400,verbose_name = "نام")
    description=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات")
    input=models.ManyToManyField(Material,null=True,blank=True,verbose_name = " قطعه ورودی ")
    output=models.ManyToManyField(Material,null=True,blank=True,verbose_name = " قطعه خروجی ")

    class Meta:
        verbose_name = "ارتبات"
        verbose_name_plural = "ارتباتاط"

    def __str__(self):
        return self.name


#------------------------------------------------------------------------------
class Product(models.Model):
    name=models.CharField(max_length=200,verbose_name = "نام")
    description=models.TextField(max_length=800,null=True,blank=True,verbose_name = "توضیحات")

    class Meta:
        verbose_name = " محصول "
        verbose_name_plural = " محصولات "

    def __str__(self):
        return self.name
