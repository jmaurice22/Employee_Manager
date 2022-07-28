from django.shortcuts import render

from .models import SupplyItem


# Create your views here.
def supplies(request):
    supplies = SupplyItem.objects.all()
    return render(request, 'supplies.html', {'supplies': supplies})

def add_supply(request):
    return render(request, 'supplies.html')
