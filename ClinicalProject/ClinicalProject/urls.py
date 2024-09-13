"""
URL configuration for ClinicalProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DoctorApp import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctors/', view=views.list_of_doctors, name='list_of_doctors' ),
    path('doctors/create/', view=views.create_doctor, name='create_doctor' ),
    path('doctors/edit/<id>/', view=views.edit_doctor, name='edit_doctor' ),
    path('doctors/edit/<id>/', view=views.delete_doctor, name='delete_doctor' ),
]
