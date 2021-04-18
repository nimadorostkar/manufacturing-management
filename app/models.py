from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from mapbox_location_field.models import LocationField
from django.dispatch import receiver
from django.db.models.signals import post_save






#------------------------------------------------------------------------------
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True,related_name='profile',verbose_name = "کاربر")
  phone = models.CharField(max_length=50,null=True, blank=True,verbose_name = " شماره تماس  ")
  address = models.CharField(max_length=3000,null=True, blank=True,verbose_name = " آدرس  ")
  user_photo = models.ImageField(upload_to='user_uploads/user_photo',default='user_uploads/user_photo/default.png',null=True, blank=True,verbose_name = "تصویر کاربر")


  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()


  def image_tag(self):
        return format_html("<img width=50 src='{}'>".format(self.user_photo.url))

  def user_name(self):
        return str(self.user)


  class Meta:
      verbose_name = "پروفایل"
      verbose_name_plural = " پروفایل ها "


  def __str__(self):
    return "پروفایل : " + str(self.user)






#------------------------------------------------------------------------------
class Station(models.Model):
    name = models.CharField(max_length=400,verbose_name = "نام")
    CHOICES = ( ('M','Material'), ('R','Repository'), ('T','Transfer'), ('S','Station') )
    position=models.CharField(max_length=1,choices=CHOICES,verbose_name = "ایستگاه")
    description=models.TextField(max_length=1000,null=True, blank=True,verbose_name = "مشخصات")
    capacity = models.IntegerField(null=True,blank=True, verbose_name = " ظرفیت ")
    manager = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True,verbose_name = "مسئول")
    inputs = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='sub_station',verbose_name = "ورودی ها")
    location = LocationField(null=True,blank=True)

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by=['name']

    class Meta:
        verbose_name = "ایستگاه"
        verbose_name_plural = " ایستگاه ها"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:stations_detail',args=[self.id])




#------------------------------------------------------------------------------
class Product(models.Model):
    name=models.CharField(max_length=400,verbose_name = "نام")
    code=models.CharField(max_length=50,null=True, blank=True,verbose_name = "کد ")
    description=models.TextField(max_length=900,null=True, blank=True,verbose_name = "توضیحات")
    image=models.ImageField(upload_to='media', default='media/Default.png' ,null=True, blank=True,verbose_name = "تصویر")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:products_detail',args=[self.id])

    def image_tag(self):
        return format_html("<img width=50 src='{}'>".format(self.image.url))




#------------------------------------------------------------------------------
# MPTT Model -->  https://django-mptt.readthedocs.io/en/latest/index.html
class Tree(MPTTModel):
    name = models.ForeignKey(Station, on_delete=models.CASCADE,verbose_name = "نام")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',verbose_name = "والد")
    relatedProduct=models.ManyToManyField(Product,verbose_name = "محصول مرتبط")
    quantity = models.IntegerField(default='1',verbose_name = "تعداد در یک محصول")

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "درخت محصول"
        verbose_name_plural = "درخت محصولات"

    def __str__(self):
        return str(self.name)

    def position(self):
        return  self.name.position




#------------------------------------------------------------------------------
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name = "کاربر")
    ticket_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300,null=True, blank=True,verbose_name = " عنوان ")
    descriptions = models.TextField(max_length=800,null=True, blank=True,verbose_name = "توضیحات")
    CHOICES1 = ( ('تیکت','تیکت'), ('پاسخ','پاسخ') )
    status = models.CharField(max_length=20,choices=CHOICES1,default='تیکت',verbose_name = "وضعیت")
    CHOICES2 = ( ('🔴New','🔴New'),('🟠checked','🟠checked'), ('Answered','Answered') )
    case = models.CharField(max_length=20,choices=CHOICES2,default='🔴New',verbose_name = "حالت")
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    def user_name(self):
          return str(self.user)

    class Meta:
        ordering = ['-created_on']

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = " Tickets "

    def __str__(self):
        return str(self.created_on)
