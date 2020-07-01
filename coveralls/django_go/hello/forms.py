from django import forms

from hello.models import Departments, Staff, Suppliers


class DepartmentsForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = ("department", )  # NOTE: the trailing comma is required


class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = ("supplier", )  # NOTE: the trailing comma is required


class Popular(forms.Form):
    popular = forms.CharField(label='', max_length=100)
