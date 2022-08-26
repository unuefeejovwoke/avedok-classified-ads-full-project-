from distutils.command.upload import upload
from msilib.schema import Condition
from time import timezone
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
class Product(models.Model):
    CONDITION_TYPE =(
        ('New','New'),
        ('Used','Used'),
    )


    def get_image_path(instance,filename):
        name, ext = filename.split('.')
        image_path = 'product_photos/{prod_name}/{photo_name}.{ext}'.format(prod_name=instance.name,photo_name=name,ext=ext)
        return image_path

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    condition = models.CharField(max_length=100,choices=CONDITION_TYPE)
    price = models.IntegerField()
    
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(default = timezone.now)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    brand = models.ForeignKey('Brand',on_delete=models.SET_NULL,null=True)
    photo_main = models.ImageField(upload_to=get_image_path)
    photo_1 = models.ImageField(upload_to=get_image_path,blank=True)
    photo_2 = models.ImageField(upload_to=get_image_path,blank=True)
    photo_3 = models.ImageField(upload_to=get_image_path,blank=True)
    photo_4 = models.ImageField(upload_to=get_image_path,blank=True)
    photo_5 = models.ImageField(upload_to=get_image_path,blank=True)
    photo_6 = models.ImageField(upload_to=get_image_path,blank=True)
    slug = models.SlugField(blank=True,null=True)
    isTrending = models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        self.slug =slugify(self.name)
        super(Product,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset
    
 
class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    owner= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    class Meta:
        unique_together = [['owner', 'product']]
    
    def __str__(self):
        return self.value


class Category(models.Model):
    ## for product category
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/', blank=True, null=True)
    
    slug = models.SlugField(blank=True, null=True) 
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)    
        super(Category ,self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name 
    

class Brand(models.Model):
    ## for product category
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
    
    def __str__(self):
        return self.name 

class Podcast(models.Model):
    name = models.CharField(max_length=100)
    podcastlink = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name 