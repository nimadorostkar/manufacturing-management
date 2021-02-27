from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse




class Place(models.Model):
    CHOICES = ( ('M','Material'), ('S','Station'), ('P','Product') )
    position=models.CharField(max_length=1, choices=CHOICES,verbose_name = "موقعیت")
    name=models.CharField(max_length=400,verbose_name = "نام")
    description=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات")
    location=models.CharField(max_length=400,verbose_name = "location")
    input=models.ManyToManyField('Place',blank=True,verbose_name = "ورودی")

    class Meta:
        verbose_name = "جایگاه"
        verbose_name_plural = " جایگاه ها"

    def __str__(self):
        return self.name

















#------------------------------------------------------------------------------
#class Material(models.Model):
    #id = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    #name=models.CharField(max_length=400,verbose_name = "نام")
    #description=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات")
    #material_input=models.ForeignKey('Material',on_delete=models.CASCADE,null=True,blank=True,verbose_name = " قطعه ورودی")
    #station_input=models.ForeignKey('Station',on_delete=models.CASCADE,null=True,blank=True,verbose_name = " ایستگاه ورودی ")

    #class Meta:
        #verbose_name = "قطعه"
        #verbose_name_plural = "قطعات"

    #def __str__(self):
        #return self.name


#------------------------------------------------------------------------------
#class Station(models.Model):
    #id = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    #name=models.CharField(max_length=400,verbose_name = "نام")
    #description=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات")
    #material_input=models.ForeignKey(Material,on_delete=models.CASCADE,null=True,blank=True,verbose_name = " قطعه ورودی")
    #station_input=models.ForeignKey('Station',on_delete=models.CASCADE,null=True,blank=True,verbose_name = " ایستگاه ورودی ")

    #class Meta:
        #verbose_name = "ایستگاه"
        #verbose_name_plural = "ایستگاه ها"

    #def __str__(self):
        #return self.name


#------------------------------------------------------------------------------
#class Relation(models.Model):
    #id = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    #name=models.CharField(max_length=400,verbose_name = "نام")
    #description=models.TextField(max_length=500,null=True,blank=True,verbose_name = "مشخصات")
    #material_input=models.ManyToManyField(Material,verbose_name =" قطعه ورودی")
    #station_input=models.ManyToManyField(Station,verbose_name = " ایستگاه ورودی ")

    #class Meta:
        #verbose_name = "رابطه"
        #verbose_name_plural = "روابط"

    #def __str__(self):
        #return self.name




#------------------------------------------------------------------------------
#class Product(models.Model):
    #id = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    #name=models.CharField(max_length=200,verbose_name = "نام")
    #description=models.TextField(max_length=800,null=True,blank=True,verbose_name = "توضیحات")
    #material_input=models.ForeignKey(Material,on_delete=models.CASCADE,null=True,blank=True,verbose_name = " قطعه ورودی")
    #station_input=models.ForeignKey(Station,on_delete=models.CASCADE,null=True,blank=True,verbose_name = " ایستگاه ورودی ")

    #class Meta:
        #verbose_name = " محصول "
        #verbose_name_plural = " محصولات "

    #def __str__(self):
        #return self.name
