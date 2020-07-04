from django.db import models

# Create your models here.
class Employees (models.Model):
    employee_name = models.CharField(max_length=100)
    employee_code = models.CharField(max_length=100)
    in_time = models.TimeField(auto_now=False, auto_now_add=False)
    out_time = models.TimeField(auto_now=False, auto_now_add=False)
    hours = models.IntegerField(blank=True,null=True)
    overtime = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.employee_name