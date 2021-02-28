from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse




#------------------------------------------------------------------------------
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
