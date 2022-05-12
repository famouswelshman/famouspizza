from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):
    cart = request.session.get('bag', {})
    if not cart:
        messages.error(request, "There is nothing in your shopping cart")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)