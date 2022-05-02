from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.


def all_products(request):
    """ Page to display all products with search function """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Page to djsplay full details of one specific product with search function """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)