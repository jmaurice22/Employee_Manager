from django.shortcuts import render, redirect
from .forms import EmployeeForm, leaveForm
from .models import Employee, leaveDate


# Create your views here.

def employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/home')

    return render(request, "employee_contact.html", {'form': form})


def employee_registration(request):
    return render(request, "employee_registration.html")


def request_time_off(request):

    #new leave instance form
    form = leaveForm()

    return render(request, 'request_time_off.html', {'form': form})
