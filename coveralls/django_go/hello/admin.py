from django.contrib import admin

from hello.models import Staff, Supp1, Supp2, JobTitles

admin.site.register(Staff)

admin.site.register(Supp1)
admin.site.register(Supp2)
admin.site.register(JobTitles)
