import re
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView

from hello.forms import DepartmentsForm, SuppliersForm
from hello.models import Staff ,Departments, Suppliers


# class HomeListView(ListView):
#     """Renders the home page, with a list of all messages."""
#     model = LogMessage

#     def get_context_data(self, **kwargs):
#         context = super(HomeListView, self).get_context_data(**kwargs)
#         return context

class DepartmentsListView(ListView):
    model = Departments

    def get_context_data(self, **kwargs):
        context = super(DepartmentsListView, self).get_context_data(**kwargs)
        return context


class StaffListView(ListView):
    model = Staff

    def get_context_data(self, **kwargs):
        context = super(StaffListView, self).get_context_data(**kwargs)
        return context


def home(request):
    return render(request,'hello/home.html')


def start_page_base_unit(request):
    return render(request, "base_unit/start_page_base_unit.html")


def add_departments(request):
    form = DepartmentsForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            departments = form.save(commit=False)
            departments.save()
            return redirect("start_page_base_unit")
    else:
        return render(request, "base_unit/add_departments.html", {"form": form})


def add_suppliers(request):
    form = SuppliersForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            suppliers = form.save(commit=False)
            suppliers.save()
            return redirect("start_page_base_unit")
    else:
        return render(request, "base_unit/add_suppliers.html", {"form": form})