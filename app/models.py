from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse





#------------------------------------------------------------------------------
class Material(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=400,verbose_name = "نام")
    description=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات")
    m_sub=models.ManyToManyField("self",blank=True,verbose_name = " قطعه ورودی")
    s_sub=models.ManyToManyField("Station",blank=True,verbose_name = " ایستگاه ورودی ")

    class Meta:
        verbose_name = "قطعه"
        verbose_name_plural = "قطعات"

    def __str__(self):
        return self.name


#------------------------------------------------------------------------------
class Station(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=400,verbose_name = "نام")
    description=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات")
    m_sub=models.ManyToManyField(Material,blank=True,verbose_name = " قطعه ورودی")
    s_sub=models.ManyToManyField("self",blank=True,verbose_name = " ایستگاه ورودی ")

    class Meta:
        verbose_name = "ایستگاه"
        verbose_name_plural = "ایستگاه ها"

    def __str__(self):
        return self.name



#------------------------------------------------------------------------------
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,verbose_name = "نام")
    description=models.TextField(max_length=800,null=True,blank=True,verbose_name = "توضیحات")
    m_sub=models.ManyToManyField(Material,blank=True,verbose_name = " قطعه ورودی")
    s_sub=models.ManyToManyField(Station,blank=True,verbose_name = " ایستگاه ورودی ")

    class Meta:
        verbose_name = " محصول "
        verbose_name_plural = " محصولات "

    def __str__(self):
        return self.name
