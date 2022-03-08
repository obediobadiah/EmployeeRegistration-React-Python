from dataclasses import field
from doctest import DocTestParser
from rest_framework import serializers
from EmployeeApp.models import Departements, Employees

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departements
        fields = '__all__'



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        # field = ('EmployeeId', 
        #         'EmployeeName', 
        #         'Departement', 
        #         'DateOfJoining', 
        #         'PhotoFileName')