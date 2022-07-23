from django.shortcuts import render


# Create your views here.
def supplies(request):
    return render(request, 'supplies.html')
