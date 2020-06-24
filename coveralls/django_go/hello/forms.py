from django import forms

from hello.models import Departments, JobTitles, LogMessage, Suppliers


class LogMessageForm(forms.ModelForm):
    pass
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required


class JobTitlesForm(forms.ModelForm):
    class Meta:
        model = JobTitles
        fields = ("job_title", )  # NOTE: the trailing comma is required


class DepartmentsForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = ("department", )  # NOTE: the trailing comma is required


class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = ("supplier", )  # NOTE: the trailing comma is required
