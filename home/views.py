from django.shortcuts import render
from django.contrib import messages

# Create your views here.


def index(request):
    messages.success(request, 'test')
    return render(request, 'home/index.html')