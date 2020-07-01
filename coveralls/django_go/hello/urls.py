from django.urls import path

from hello import views
from hello.models import Staff, Departments, Suppliers

# home_list_view = views.HomeListView.as_view(
#     # :5 limits the results to the five most recent
#     queryset=LogMessage.objects.order_by("-log_date")[:5],
#     context_object_name="message_list",
#     template_name="hello/home.html",
# )

staff_list_view = views.StaffListView.as_view(
    queryset=Staff.objects.all(),
    context_object_name='staff',
    template_name='base_unit/add_departments.html'
    )


urlpatterns = [
    # Replace the existing path for ""
    path("", views.home, name="home"),
    path("start_page_base_unit/",
         views.start_page_base_unit,
         name="start_page_base_unit"),
    path("add_departments/", staff_list_view, name="add_departments"),
    # path("add_departments/", views.add_departments, name="add_departments"),
    path("add_suppliers/", views.add_suppliers, name="add_suppliers"),
]
