from django import forms
from django.forms import ModelForm
from .models import *
import datetime


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email', 'phone_number')

    widgets = {
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'phone_number': forms.TextInput(attrs={'class': 'form-control', }),
    }


class leaveForm(forms.Form):
    start_date = forms.DateField(initial=datetime.date.today)
    end_date = forms.DateField(initial=datetime.date.today() + datetime.timedelta(days=1))
    comment = forms.CharField(widget=forms.Textarea)
