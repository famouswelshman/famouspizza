from django.shortcuts import render
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'home/index.html')