from django.contrib import admin

# Register your models here.
from .models import Product, Category, Brand, Review, Podcast

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Podcast)
