from django.shortcuts import render
from employee.models import Employee
import datetime

# Create your views here.


def home(request):
    employees = Employee.objects.all()

    date = datetime.datetime.now()
    dates = date.strftime("%B %d, %Y")
    return render(request, 'home.html', {'employees': employees, 'date': dates})
