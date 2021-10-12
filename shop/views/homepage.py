from django.shortcuts import render
from ..models import product, customer, category
from django.db.models import Count

def homepage(request):
    products = product.Product.objects.all()
    Categories = category.Category.objects.all().annotate(products_count = Count('product'))
    customers = customer.Customer.objects.all()
    return render(request, 'index.html', {'Categories':Categories, 'customers':customers, 'products':products, 'all_products':products})