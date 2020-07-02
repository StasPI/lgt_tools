from django.urls import path

from hello import views
from hello.models import Departments, Staff, Suppliers

# staff_list_view = views.StaffListView.as_view(
#     queryset=Staff.objects.all(),
#     context_object_name='staff',
#     template_name='base_unit/add_departments.html'
#     )

urlpatterns = [
    # Replace the existing path for ""
    path("", views.home, name="home"),
    path("start_page_base_unit/",
         views.start_page_base_unit,
         name="start_page_base_unit"),

    # path("add_departments/", staff_list_view, name="add_departments"),
    # path("add_departments/", views.add_departments, name="add_departments"),
    path("add_departments/", views.get_popular, name="add_departments"),
    path("add_suppliers/", views.add_suppliers, name="add_suppliers"),
]
