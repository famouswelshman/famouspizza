from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)

from django.contrib import messages
from products.models import Product

# Create your views here.

def view_cart(request):
    """ This view shows the cart contents page """
    
    return render(request, 'cart/cart.html')

    
def add_to_cart(request, item_id):
    """ Adding a product to the cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})
    
    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 (f'Updated size {size.upper()} '
                                  f'{product.name} quantity to '
                                  f'{cart[item_id]["items_by_size"][size]}'))
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(request,
                                 (f'Added size {size.upper()} '
                                  f'{product.name} to your bag'))
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             (f'Added size {size.upper()} '
                              f'{product.name} to your cart'))
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {cart[item_id]}'))
        
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)
    

def remove_from_cart(request, item_id):
    """ Remove product from cart """

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
                         
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)
        
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)