# PatientApp/forms.py

from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'name', 
            'disease', 
            'age', 
            'mobile_number', 
            'accompanying_person_name', 
            'accompanying_person_contact', 
            'accompanying_person_relation'
        ]
