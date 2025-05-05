from django.shortcuts import render, redirect
from .models import Doctor
# Create your views here.
def list_of_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'list.html', {'doctors' : doctors})

def create_doctor(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    elif request.method == 'POST':
        name = request.POST['name'] 
        specialization = request.POST['specialization'] 
        year_of_experience = request.POST['year_of_experience'] 
        doctor = Doctor(name = name, specialization = specialization, year_of_experience = year_of_experience)
        doctor.save()
        return redirect('list_of_doctors')         

def edit_doctor(request, id):
    if request.method == 'GET':
        doctor = Doctor.objects.get(id = id)
        return render(request, 'edit.html', {'doctor' :doctor})
    elif request.method == 'POST':
        doctor = Doctor.objects.get(id = id)
        doctor.name = request.POST['name'] 
        doctor.specialization = request.POST['specialization'] 
        doctor.year_of_experience = request.POST['year_of_experience'] 
        doctor.save()
        return redirect('list_of_doctors')    
        
def delete_doctor(request, id):
    doctor = Doctor.objects.get(id = id)
    doctor.delete()
    return redirect('list_of_doctors')
