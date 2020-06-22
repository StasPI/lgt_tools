import re
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView

from hello.forms import DepartmentsForm, JobTitlesForm, LogMessageForm
from hello.models import Departments, JobTitles, LogMessage


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def about(request):
    return render(request, "hello/about.html")


def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})


def job_titles(request):
    form = JobTitlesForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            job_title = form.save(commit=False)
            job_title.save()
            return redirect("home")
    else:
        return render(request, "hello/job_titles.html", {"form": form})


def departments(request):
    form = DepartmentsForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            departments = form.save(commit=False)
            departments.save()
            return redirect("home")
    else:
        return render(request, "hello/departments.html", {"form": form})
