from django.shortcuts import render, redirect
from ..models.product import Product 
from ..views import category
from django.db.models import Count
from ..models import product

def search (request):
    if request.method == 'POST':
        searched_product_from_input = request.POST.get("searched_product").title()
        print (searched_product_from_input)
        searched_products = Product.objects.filter(name__contains = searched_product_from_input )
        Categories = category.Category.objects.all().annotate(products_count = Count('product'))
        products = product.Product.objects.all()
        return render(request,'search.html', {'searched_product_from_input':searched_product_from_input, 'searched_products': searched_products, 'Categories':Categories, 'all_products':products })