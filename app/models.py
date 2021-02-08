from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse


class Product(models.Model):
    id=models.AutoField(primary_key=True,verbose_name = "شناسه")
    pid=models.CharField(max_length=100,verbose_name = "زیر شاخه")
    name=models.CharField(max_length=100,verbose_name = "نام")
    title=models.CharField(max_length=100,verbose_name = "تیتر")
    image=models.ImageField(upload_to='image',verbose_name = "تصویر")
    content=models.TextField(max_length=500,verbose_name = "مشخصات")
    tag=models.CharField(max_length=200,verbose_name = "برچسب")


    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name
