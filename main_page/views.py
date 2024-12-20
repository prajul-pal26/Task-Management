from ast import Index
from django.http import HttpResponse
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import authentication, Employee, Task
# from .forms import TaskForm, EmployeeForm,UpdateForm, UpdateForm_employee
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re
from .serializers import AuthenticationModel, EmployeeModel, TaskModel
from rest_framework import viewsets 


class AuthViewSet(viewsets.ModelViewSet):
    queryset = authentication.objects.all() 
    serializer_class = AuthenticationModel

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()  
    serializer_class = EmployeeModel
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  
    serializer_class = TaskModel

def login(request, id):
    request.session['is_logged_in']= False
    if request.method == "POST" and 'name' in request.POST:
        name=request.POST['name']    
        email = request.POST.get('email')
        user=authentication.objects.filter(name=name, email=email)
    
        if user:           
            request.session['is_logged_in']= True
            import email_sender
            request.session['otp'] = email_sender.Email().send_email(send_email_to=email)
            return render(request,"login.html",{'id': 1}) 
            
        else: 
            messages.info(request,'Credentials Invalid')
            return render(request,"login.html",{'id': 0})      
         
    elif request.method == "POST" and 'otp' in request.POST:
        otp=request.POST['otp']    
    
        if otp == request.session['otp']:           
            return HttpResponse("sedredsrfe")
        else: 
            messages.info(request,'Credentials Invalid')
            return render(request,"login.html",{'id': 0}) 
        
    return render(request,"login.html",{'id': id})

def signup(request):
    if request.method == "POST":
        name=request.POST['name']  
        email = request.POST['email']
        password=request.POST['password']  
        password2=request.POST['password2'] 
        
        if password==password2:
            
            if authentication.objects.filter(name=name).exists():
                messages.info(request,"username Taken")
                return redirect('signup')
            else:
                user=authentication.objects.create(name= name, email= email, password= password)
                user.save()
                
                return redirect("/login")
        else:
            messages.info(request,'Password Not Matching')
            return redirect('signup')                                         
    else:
        return render(request, "signup.html")

def hello(request):
    return HttpResponse("Hello!")

def employer_dashboard(request):
    if request.session['is_logged_in'] is True:
        tasks = Task.objects.filter(employer=request.user)
        employees = Employee.objects.all() 
        return render(request, 'employer_dashboard.html', {'tasks': tasks, 'employees': employees})
    return render(request,"login.html")

@login_required(login_url='login')
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.employer = request.user 
            task.save()
            messages.success(request, 'Task added and assigned successfully!')
            return redirect('employer_dashboard')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

@login_required(login_url='login')
def task_list(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(employer=request.user)
    else:
        tasks = Task.objects.none()  
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required(login_url='login')
def delete_selected_tasks(request,id):
    dele =Task.objects.get(id=id)
    dele.delete()
    return redirect('/task_list')

@login_required(login_url='login')
def update(request, id):
    data =  Task.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/task_list')  
    else:
        form = UpdateForm(instance=data)
    return render(request, 'update_task.html', {'form': form})
#----------------------------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.employer = request.user  
            employee.save()
            messages.success(request, 'Employee added successfully!')
            return redirect('employer_dashboard') 
        else:
            messages.error(request, 'There was an error with the form.')
    else:
        form = EmployeeForm()
    
    return render(request, 'add_employee.html', {'form': form})

@login_required(login_url='login')
def employee_list(request):
    if request.user.is_authenticated:
        employees = Employee.objects.filter(employer=request.user)
    else:
        employees = Employee.objects.none() 
    return render(request, 'employee_list.html', {'employees': employees})

@login_required(login_url='login')
def delete_selected_employee(request,id):
    dele =Employee.objects.get(id=id)
    dele.delete()
    return redirect('/employee_list')

@login_required(login_url='login')
def update_employee(request, id):
    data =  Employee.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateForm_employee(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/employee_list')  
    else:
        form = UpdateForm_employee(instance=data)
    
    return render(request, 'update_employee.html', {'form': form})
    
 