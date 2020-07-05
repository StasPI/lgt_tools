from django.urls import path

from hello import views
from hello.models import Staff, Supp1, Supp2, JobTitles

job_titles_view = views.JobTitlesView.as_view(
    queryset=JobTitles.objects.all(),
    context_object_name='JobTitles',
    template_name='base_unit/add_job_titles.html')

urlpatterns = [
    # cover page
    path("", views.home, name="home"),
    path("start_page_base_unit/",
         views.start_page_base_unit,
         name="start_page_base_unit"),
    # test page
    path("add_job_titles/", job_titles_view, name="add_job_titles"),
    path("add_departments/", views.get_popular, name="add_departments"),
]
