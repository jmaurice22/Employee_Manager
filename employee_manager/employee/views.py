from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


# Create your views here.

def employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/home')

    return render(request, "employee.html", {'form': form})


def employee_registration(request):
    return render(request, "employee_registration.html")


