from django.contrib import admin

from hello.models import Departments, Staff, Suppliers

admin.site.register(Departments)
admin.site.register(Suppliers)
admin.site.register(Staff)
