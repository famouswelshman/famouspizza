from django.urls import path
from . import views


urlpatterns=[
    path('', views.deals, name='deals')
]