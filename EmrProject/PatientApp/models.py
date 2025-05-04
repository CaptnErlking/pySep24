from django.db import models
from django.utils import timezone

class Patient(models.Model):
    name = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    mobile_number = models.CharField(max_length=15, blank=True, null=True)

    accompanying_person_name = models.CharField(max_length=100, blank=True, null=True)
    accompanying_person_relation = models.CharField(max_length=50, blank=True, null=True)
    accompanying_person_contact = models.CharField(max_length=15, blank=True, null=True)

    doctor_name = models.CharField(max_length=100, default="Dr. Kritika Sarkar")

    custom_id = models.CharField(max_length=255, unique=True, null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.custom_id:
            current_year = timezone.now().year
            count = Patient.objects.filter(custom_id__startswith=f'NammaClinic_{current_year}').count() + 1
            self.custom_id = f'NammaClinic{current_year}{count:03d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.custom_id})"
