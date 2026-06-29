from django.db import models

# Create your models here.
class Site(models.Model):
    site_title = models.CharField(max_length=100,verbose_name='عنوان')
    site_des = models.TextField(verbose_name='توضیحات')
    github_link = models.URLField(verbose_name='یو آر ال')
    is_active=models.BooleanField(default=True,verbose_name='فعال بودن')

class Maker(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام')
    lastname = models.CharField(max_length=100,verbose_name='نام خانوادگی')
    github = models.CharField(max_length=600,verbose_name='لینک گیتهاب' , null=True,blank=True)
    site = models.CharField(max_length=600,verbose_name='لینک سایت' , null=True,blank=True)