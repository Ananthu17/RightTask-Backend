from rest_framework import serializers
from .models import Employees

class Employeesserializers(serializers.ModelSerializer):
    class Meta :
        model= Employees
        fields = ['id','employee_name','employee_code','in_time','out_time','hours','overtime']

