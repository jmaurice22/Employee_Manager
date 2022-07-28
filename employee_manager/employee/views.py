from django.shortcuts import render, redirect
from .forms import EmployeeForm, leaveForm
from .models import Employee, leaveDate


def employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/home')

    return render(request, "employee_contact.html", {'form': form})


def employee_registration(request):
    requests = leaveDate.objects.all()
    return render(request, "employee_registration.html", {'requests': requests})


def request_time_off(request):
    form = leaveForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/home')

    return render(request, 'request_time_off.html', {'form': form})
