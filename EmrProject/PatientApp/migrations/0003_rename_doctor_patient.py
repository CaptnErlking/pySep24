# Generated by Django 5.1.1 on 2024-09-13 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientApp', '0002_rename_year_of_experience_doctor_age_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctor',
            new_name='Patient',
        ),
    ]
