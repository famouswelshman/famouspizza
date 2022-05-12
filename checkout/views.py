from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your shopping cart")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KycscFC5DY9G8LxLFtY5EEwxdz1Nzup83RAQ70NgjgYNzEwlKjVuEbzpPqIkwvHQPCA2MA4HaYAhV6ZYAEIeRST0084k2ujKw',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)