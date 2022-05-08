from django.shortcuts import render
from .models import Deals




def deals(request):
    all_deals = Deals.objects.all()

    context = {
        'all_deals': all_deals,
    }

    return render(request, 'deals/deals.html', context)

def deal_detail(reques):
    """ Page to djsplay full details of one specific product with search function """

    deal = get_object_or_404(Deal, pk=deal_id)

    context = {
        'deal': deal,
    }

    return render(request, 'products/product_detail.html', context)