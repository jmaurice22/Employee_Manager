from django.urls import path
from . import views

urlpatterns = [
    path('', views.supplies, name='supplies'),
    path('add_supply', views.add_supply, name='add_supply')
]
