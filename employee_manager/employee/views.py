from django.shortcuts import render
from .forms import EmployeeForm


# Create your views here.

def employee(request):
    form = EmployeeForm()

    return render(request, "employee.html", {'form': form})
