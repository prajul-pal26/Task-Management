from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employees", default=1)  
    name = models.CharField(max_length=100,default="admin")
    phone_number = models.CharField(max_length=15)
    designation = models.CharField(max_length=100, default="employee")

    def __str__(self):
        return self.name


class Task(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employer_tasks")  
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee_tasks")
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
