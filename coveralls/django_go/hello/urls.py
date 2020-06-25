from django.urls import path

from hello import views
from hello.models import Departments, JobTitles, LogMessage, Suppliers

home_list_view = views.HomeListView.as_view(
    # :5 limits the results to the five most recent
    queryset=LogMessage.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="hello/home.html",
)


urlpatterns = [
    # Replace the existing path for ""
    path("", home_list_view, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("Hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("log/", views.log_message, name="log"),
    
    path("start_page_base_unit/",
         views.start_page_base_unit,
         name="start_page_base_unit"),
    path("add_job_titles/", views.add_job_titles, name="add_job_titles"),
    path("add_departments/", views.add_departments, name="add_departments"),
    path("add_suppliers/", views.add_suppliers, name="add_suppliers"),
]
