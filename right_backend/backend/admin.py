from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['employee_name','employee_code','in_time','out_time','hours','overtime']

admin.site.register(Employees,EmployeesAdmin)