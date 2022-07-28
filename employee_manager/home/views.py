from django.db.models.base import Model
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from employee.models import Employee, leaveDate
from employee.forms import EmployeeForm
from supplies.models import SupplyItem
import datetime


def home(request):
    employees = Employee.objects.all()
    date = datetime.datetime.now()
    supplies = SupplyItem.objects.all()
    dates = date.strftime("%B %d, %Y")
    leave_requests = leaveDate.objects.all()
    content = {
        'employees': employees,
        'supplies': supplies,
        'date': dates,
        'leave_requests': leave_requests,
    }
    return render(request, 'home.html', content)


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('/home')


def update_employee(request, id):
    obj = get_object_or_404(Employee, id=id)
    form = EmployeeForm(instance=obj)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/home')

    content = {
         'form': form,
    }
    return render(request, "employee_contact.html", content)

