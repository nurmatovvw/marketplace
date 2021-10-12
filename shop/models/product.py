from django.db import models
from .category import Category
from django.db.models import Count

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default='', blank=True, null=True)
    image = models.ImageField(upload_to='upload/products')

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
Category.objects.all().annotate(product_count=Count('product'))
s = Category.objects.all().annotate(product_count=Count('product'))