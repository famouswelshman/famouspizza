from django.shortcuts import render
from .models import Deals




def deals(request):
    all_deals = Deals.objects.all()

    context = {
        'all_deals': all_deals,
    }

    return render(request, 'deals/deals.html', context)