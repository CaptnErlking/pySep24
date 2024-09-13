from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Patient ######
# Create your views here.
def list_of_patients(request):
    patients = Patient.objects.all() ######
    return render(request, 'list.html', {'patients' : patients}) ######

def create_patient(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    elif request.method == 'POST':
        name = request.POST['name'] 
        disease = request.POST['disease'] 
        age = request.POST['age'] 
        patient = Patient(name = name, disease = disease, age = age)
        patient.save()
        return redirect('list_of_patients')         

def edit_patient(request, id):
    if request.method == 'GET':
        patient = Patient.objects.get(id = id)
        return render(request, 'edit.html', {'patient' :patient})
    elif request.method == 'POST':
        patient = Patient.objects.get(id = id)
        patient.name = request.POST['name'] 
        patient.disease = request.POST['disease'] 
        patient.age = request.POST['age'] 
        patient.save()
        return redirect('list_of_patients')    

        
def delete_patient(request, id):
    patient = Patient.objects.get(id = id)
    patient.delete()
    return redirect('list_of_patients')