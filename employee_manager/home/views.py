from django.db.models.base import Model
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from employee.models import Employee
from employee.forms import EmployeeForm
import datetime


def home(request):
    employees = Employee.objects.all()
    date = datetime.datetime.now()
    dates = date.strftime("%B %d, %Y")
    return render(request, 'home.html', {'employees': employees, 'date': dates})


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

