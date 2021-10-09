from django.shortcuts import render
from employee.models import Employee


# Create your views here.


def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})
