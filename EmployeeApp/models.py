from datetime import datetime
from enum import auto
from msilib.schema import Class
from operator import truediv
from django.db import models

# Create your models here.


class Departements(models.Model):
    DepartementId = models.AutoField(primary_key=True)
    DepartementName = models.CharField(max_length=255)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=255)
    Departement = models.CharField(max_length=255)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=255)

