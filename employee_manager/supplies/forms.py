from django import forms
from django.forms import ModelForm

from .models import SupplyItem


class SupplyItemForm(ModelForm):
    class Meta:
        model = SupplyItem
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }