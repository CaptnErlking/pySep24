from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, AuditLog  # Include AuditLog
from .forms import PatientForm
from django.contrib import messages

def list_patients(request):
    patients = Patient.objects.all().order_by('-created_at')
    return render(request, 'list_patients.html', {'patients': patients})

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            AuditLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                action='CREATE',
                model_name='Patient',
                object_id=str(patient.pk),
                object_repr=str(patient),
            )
            messages.success(request, 'Patient added successfully.')
            return redirect('list_patients')
    else:
        form = PatientForm()
    return render(request, 'create_patient.html', {'form': form})

def edit_patient(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            updated_patient = form.save()
            AuditLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                action='UPDATE',
                model_name='Patient',
                object_id=str(updated_patient.pk),
                object_repr=str(updated_patient),
            )
            return redirect('list_patients')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'edit_patient.html', {'form': form, 'patient': patient})

def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        AuditLog.objects.create(
            user=request.user if request.user.is_authenticated else None,
            action='DELETE',
            model_name='Patient',
            object_id=str(patient.pk),
            object_repr=str(patient),
        )
        patient.delete()
        messages.success(request, 'Patient deleted successfully.')
        return redirect('list_patients')
    return render(request, 'confirm_delete.html', {'patient': patient})
