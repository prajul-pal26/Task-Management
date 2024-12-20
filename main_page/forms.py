from django import forms
# from .models import Task, Employee
from django.contrib.auth.models import User

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'due_date', 'employee', 'completed']
#         widgets = {
#             'due_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
#         }

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = ['name', 'phone_number', 'designation']

# class UpdateForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = '__all__'
#         widgets = {
#             'due_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
#         }
# class UpdateForm_employee(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = '__all__'
        