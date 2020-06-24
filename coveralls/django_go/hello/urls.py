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
    path("job_titles/", views.job_titles, name="job_titles"),
    path("departments/", views.departments, name="departments"),
    path("suppliers/", views.suppliers, name="suppliers"),
    path("start_page_base_unit/",
         views.start_page_base_unit,
         name="start_page_base_unit")
]
