from django.urls import path, re_path
from EmployeeApp import views

urlpatterns=[
    path('departement/',views.DepartementApi),
    re_path(r'^departement/([0-9]+)/$', views.DepartementApi),

    path('employee/',views.EmployeeApi),
    re_path(r'^employee/([0-9]+)/$', views.EmployeeApi),
]