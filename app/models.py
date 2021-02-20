from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse


class Product(models.Model):
    name=models.CharField(max_length=200,verbose_name = "نام")
    description=models.TextField(max_length=800,null=True, blank=True,verbose_name = "توضیحات")
    input=models.ManyToManyField(Material,verbose_name = " قطعه ")


    class Meta:
        verbose_name = " محصول "
        verbose_name_plural = " محصولات "


    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('App:product_detail',args=[self.id])
