from django.db import models
from django.utils import timezone


class LogMessage(models.Model):
    message = models.CharField(max_length=200)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

# Create your models here.

class Departments(models.Model):
    id_departments = models.AutoField(primary_key=True)
    department = models.CharField(max_length=200, help_text="Enter field documentation")

    def __str__(self):
        return f'{self.department}'


class JobTitles(models.Model):
    id_job_title = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=200)
    departments = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.job_title}'


# class Staff(models.Model):
#     personnel_number = models.PositiveIntegerField()
#     full_name = models.CharField(max_length=100)
#     email_adress = models.EmailField()
#     department = models.CharField(max_length=200, primary_key=True)
#     job_title = models.CharField(max_length=200, primary_key=True)

    
class Suppliers(models.Model):
    supplier = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return f'{self.supplier}'
    