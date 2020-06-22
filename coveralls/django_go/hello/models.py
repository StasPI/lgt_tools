from django.db import models
from django.utils import timezone


class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

# Create your models here.

class JobTitles(models.Model):
    job_title = models.CharField(max_length=300, primary_key=True)

    def __str__(self):
        return f"'{self.job_title}'"
    
    
class Departments(models.Model):
    department = models.CharField(max_length=300, primary_key=True)

    def __str__(self):
        return f"'{self.department}'"
    


# class Users(models.Model):
#     full_name
#     department
#     job_title
