from django.shortcuts import render
import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.conf import settings

# Create your views here.

class main_class(APIView):
    def get(self,request):
        emp=Employees.objects.all()
        serilazer=Employeesserializers(emp,many=True)
        return Response(serilazer.data)

    def post(self,request):
        if request.method =="POST":
            received_data=json.loads(request.body)
            print(received_data['name'])
            hours=int(received_data['otime'][0:2])-int(received_data['itime'][0:2])
            print(hours)
            if hours > 8:
                overtime = hours -8
            else:
                overtime = 0
            new_emp = Employees(employee_name=received_data['name'],employee_code=received_data['code'],in_time=received_data['itime'],out_time=received_data['otime'],hours=hours,overtime=overtime)
            new_emp.save()
            emp=Employees.objects.all()
            serilazer=Employeesserializers(emp,many=True)
            return Response(serilazer.data)
            
        