from django.shortcuts import render
from .forms import EmployeeForm


# Create your views here.

def employee(request):
    form = EmployeeForm()

    return render(request, "employee.html", {'form': form})


def employee_registration(request):
    return render(request, "employee_registration.html")

#TODO: create a view to add new employee from form


