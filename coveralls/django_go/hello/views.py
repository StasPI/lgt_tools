import re
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView

from hello.forms import PopularForm
from hello.models import Staff, Supp1, Supp2, JobTitles

# class StaffListView(ListView):
#     model = Staff

#     def get_context_data(self, **kwargs):
#         context = super(StaffListView, self).get_context_data(**kwargs)
#         return context


def home(request):
    return render(request, 'hello/home.html')


def start_page_base_unit(request):
    return render(request, "base_unit/start_page_base_unit.html")


# # def add_departments(request):
# #     form = DepartmentsForm(request.POST or None)

# #     if request.method == "POST":
# #         if form.is_valid():
# #             departments = form.save(commit=False)
# #             departments.save()
# #             return redirect("add_departments")
# #         else:
# #             return render(request, "base_unit/add_departments.html",
# #                           {"form": form})
# #     else:
# #         return render(request, "base_unit/add_departments.html",
# #                       {"form": form})

# def add_suppliers(request):
#     form = PopularForm(request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             suppliers = form.save(commit=False)
#             suppliers.save()
#             return redirect("add_suppliers")
#         else:
#             return render(request, "base_unit/add_suppliers.html",
#                           {"form": form})
#     else:
#         return render(request, "base_unit/add_suppliers.html", {"form": form})

# ------------------------------------------------------------------------------------------
# пример выборки из 2 баз в одну по id
# ------------------------------------------------------------------------------------------


def get_popular(request):
    form = PopularForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            departments = form.save(commit=True)
            departments.save()
            return redirect("add_departments")
        else:
            return render(request, "base_unit/add_departments.html",
                          {"form": form})
    else:
        return render(request, "base_unit/add_departments.html",
                      {"form": form})


class JobTitlesView(ListView):
    model = JobTitles

    def get_context_data(self, **kwargs):
        context = super(JobTitlesView, self).get_context_data(**kwargs)
        return context