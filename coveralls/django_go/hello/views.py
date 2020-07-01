import re
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView

from hello.forms import DepartmentsForm, Popular, SuppliersForm
from hello.models import Departments, Staff, Suppliers

# class HomeListView(ListView):
#     """Renders the home page, with a list of all messages."""
#     model = LogMessage

#     def get_context_data(self, **kwargs):
#         context = super(HomeListView, self).get_context_data(**kwargs)
#         return context


def get_popular(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Popular(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Popular()
    return render(request, 'base_unit/add_departments.html', {'form': form})


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
    return render(request, 'hello/home.html')


def start_page_base_unit(request):
    return render(request, "base_unit/start_page_base_unit.html")


def add_departments(request):
    form = DepartmentsForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            departments = form.save(commit=False)
            departments.save()
            return redirect("add_departments")
    else:
        return render(request, "base_unit/add_departments.html",
                      {"form": form})


def add_suppliers(request):
    form = SuppliersForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            suppliers = form.save(commit=False)
            suppliers.save()
            return redirect("add_suppliers")
    else:
        return render(request, "base_unit/add_suppliers.html", {"form": form})
