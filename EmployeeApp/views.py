import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departements, Employees
from EmployeeApp.serializers import DepartementSerializer, EmployeeSerializer

@csrf_exempt
def DepartementApi(request, id=0):
    if request.method == 'GET':
        departements = Departements.objects.all()
        departement_serializer = DepartementSerializer(departements, many = True)
        return JsonResponse(departement_serializer.data, safe = False)


    elif request.method == 'POST':
        departements_data = JSONParser().parse(request)
        departement_serializer = DepartementSerializer(data=departements_data)
        if departement_serializer.is_valid():
            departement_serializer.save()
            return JsonResponse('Added successfully', safe = False)
        return JsonResponse('Failed to save', safe = False)
    

    elif request.method == 'PUT':
        departements_data = JSONParser().parse(request)
        departement = Departements.objects.get(DepartementId = departements_data['DepartementId'])
        departement_serializer = DepartementSerializer(departement, data=departements_data)
        if departement_serializer.is_valid():
            departement_serializer.save()
            return JsonResponse('Data updated successfully', safe = False)
        return JsonResponse('Failed to update', safe = False)


    elif request.method == 'DELETE':
        departement = Departements.objects.get(DepartementId = id)
        departement.delete() 
        return JsonResponse('Data deleted successfully', safe = False)



@csrf_exempt
def EmployeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employee_serializer = EmployeeSerializer(employees, many = True)
        return JsonResponse(employee_serializer.data, safe = False)


    elif request.method == 'POST':
        employees_data = JSONParser().parse(request)
        employee_serializer = DepartementSerializer(data=employees_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Added successfully', safe = False)
        return JsonResponse('Failed to save', safe = False)
    

    elif request.method == 'PUT':
        employees_data = JSONParser().parse(request)
        employee = Departements.objects.get(EmployeeId = employees_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee, data=employees_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Data updated successfully', safe = False)
        return JsonResponse('Failed to update', safe = False)


    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId = id)
        employee.delete() 
        return JsonResponse('Data deleted successfully', safe = False)




# Create your views here.
