from rest_framework import serializers 
from .models import authentication,Employee,Task

class AuthenticationModel(serializers.ModelSerializer):
    class Meta:
        model = authentication
        fields = '__all__' 
        
class EmployeeModel(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__' 
        
class TaskModel(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' 
