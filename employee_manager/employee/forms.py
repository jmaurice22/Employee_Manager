from django import forms

from .models import *


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email', 'phone_number')

    widgets = {
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
    }