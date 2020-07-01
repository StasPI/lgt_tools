from django import forms

from hello.models import Departments, Suppliers


class DepartmentsForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = ("department", )  # NOTE: the trailing comma is required


class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = ("supplier", )  # NOTE: the trailing comma is required
