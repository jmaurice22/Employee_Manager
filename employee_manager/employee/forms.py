from django import forms

from .models import *


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

# todo: add widgets dictionary to style form fields
