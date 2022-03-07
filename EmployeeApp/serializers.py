from dataclasses import field
from doctest import DocTestParser
from rest_framework import serializers
from EmployeeApp.models import Departements, Employees

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departements
        field = ('DepartementId', 
                'DepartementName')



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        field = ('EmployeeId', 
                'EmployeeName', 
                'Departement', 
                'DateOfJoining', 
                'PhotoFileName')