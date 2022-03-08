from xml.dom.minidom import Document
from django.urls import path, re_path
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

from EmployeeApp import views

urlpatterns = [

    path('departement',views.DepartementApi),
    re_path(r'^departement/([0-9]+)/$', views.DepartementApi),

    path('employee',views.EmployeeApi),
    re_path(r'^employee/([0-9]+)/$', views.EmployeeApi),
    
    re_path(r'^Employee/SaveFile$', views.SaveFile),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)