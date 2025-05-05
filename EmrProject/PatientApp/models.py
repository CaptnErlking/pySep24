from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    model_name = models.CharField(max_length=100)
    object_id = models.CharField(max_length=100)
    object_repr = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.timestamp} - {self.action} - {self.model_name} ({self.object_id})"


class PatientIDCounter(models.Model):
    year = models.IntegerField(unique=True)
    counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.year} - {self.counter}"


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
            counter_obj, _ = PatientIDCounter.objects.get_or_create(year=current_year)
            counter_obj.counter += 1
            counter_obj.save()
            self.custom_id = f'NammaClinic{current_year}{counter_obj.counter:03d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.custom_id})"
