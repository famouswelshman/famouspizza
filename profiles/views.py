from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def profile(request):
    """ Displays user profile """

    template = 'profiles/profile.html'
    context = {}


    return render(request, template, context)