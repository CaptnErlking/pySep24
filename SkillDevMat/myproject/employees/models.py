from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
            return f'[id = {self.id}, name = {self.name}]'

class Employee(models.Model) : 
    name = models.CharField(max_length=255)
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    bonus = models.FloatField()
    
    def __str__(self):
            return f'{self.name} - {self.job_title} - earns : {self.salary} - bonus : {self.salary}'