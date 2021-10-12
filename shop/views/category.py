from ..models.product import Product
from django.shortcuts import render
from ..models.category import Category
from django.db.models import Count

def pr_by_category(request, pk):
    all_products = Product.objects.all()
    products = Product.objects.filter(category=pk)
    Categories = Category.objects.all().annotate(products_count = Count('product'))

    return render(request, 'index.html', {'products':products, 'Categories':Categories, 'all_products':all_products})
    