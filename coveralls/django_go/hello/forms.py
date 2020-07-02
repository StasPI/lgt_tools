from django import forms

from hello.models import Departments, Staff, Suppliers


class DepartmentsForm(forms.ModelForm):
    #форма прямого ввода
    class Meta:
        model = Departments
        fields = ("department", )


class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = ("supplier", )


class PopularForm(forms.ModelForm):
    # форма выбора из бд
    popular = forms.ModelChoiceField(queryset=Staff.objects.values())
    # popular = forms.ModelMultipleChoiceField(queryset=Staff.objects.all())
    class Meta:
        model = Departments
        fields = ("popular",)