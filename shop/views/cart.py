from django.shortcuts import redirect, render
from ..models.product import Product 

def cart(request):
    cart_session = request.session.get('cart_session', [])
    all_products_count = len(cart_session)
    products_cart = Product.objects.filter(id__in=cart_session)
    price = 0
    
    for product_cart in products_cart:
        product_cart.count = cart_session.count(product_cart.id)
        product_cart.sum = product_cart.count * product_cart.price
        price += product_cart.sum

    return render(request, 'cart.html', {'products': products_cart, 'cart_session':cart_session, 'all_products_count':all_products_count,'price':price})

    

def addToCart(request, pk):
    cart_session = request.session.get('cart_session', [])
    cart_session.append(pk)
    request.session['cart_session'] = cart_session
    return redirect('/')
 
def remove_from_cart (request, pk):
    cart = request.session.get('cart_session', [])
    new_cart = []
    for fk in cart:
        if fk != pk:
            new_cart.append(fk)
    
    request.session['cart_session']= new_cart
    return redirect('cart')