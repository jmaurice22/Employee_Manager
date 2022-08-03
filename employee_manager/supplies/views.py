from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import SupplyItemForm

from .models import SupplyItem


# Create your views here.
def supplies(request):
    supplies = SupplyItem.objects.all()
    return render(request, 'supplies.html', {'supplies': supplies})

def add_supply(request):
    form = SupplyItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/supplies')     
    return HttpResponse('Add Supply')
