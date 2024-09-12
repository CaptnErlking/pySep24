from django.shortcuts import render

# Create your views here.
from .models import Doctor 

def list_of_doctors(request):
    return render(request,'list.html')
    #doctors = Doctor.objects.all()
    #code 
    #connect to the template "list.html" takes "doctors" as param

def create_doctor(request):
    return render(request,'form.html')
    #GET method
        #connect to the template "form.html" 
    #POST method 
        # name 
        # specialization
        # year_of_experience
        # doctor = Doctor(name = name, specialization = specialization, year_of_experience = year_of_experience)
        # doctor.save()
        #redirect list page 

def edit_doctor(request, id):
    return render(request,'form.html')
    #GET method
        # doctor = Doctor.objects.get(id = id)
        #connect to the template "form.html" pass doctor as param  
    #POST method 
        # doctor = Doctor.objects.get(id = id)
        # doctor.name =  
        # doctor.specialization
        # doctor.year_of_experience
        # doctor.save()
        # #redirect list page 
        
def delete_doctor(request, id):
    return redirect('list_of_doctors')
    # doctor = Doctor.objects.get(id = id)
    # doctor.delete()
    #redirect list page 
