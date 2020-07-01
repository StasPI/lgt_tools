from django.db import models
from django.utils import timezone


class Departments(models.Model):
    id_departments = models.AutoField(primary_key=True)
    department = models.CharField(max_length=200, help_text="Enter field documentation")

    def __str__(self):
        return f'{self.department}'


class Staff(models.Model):
    personnel_number = models.PositiveIntegerField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email_adress = models.EmailField()
    department = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.job_title, self.full_name, self.email_adress, self.department, self.job_title}'


class Suppliers(models.Model):
    supplier = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return f'{self.supplier}'
