from ast import Index
from django.http import HttpResponse
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Employee
from .forms import TaskForm, EmployeeForm,UpdateForm, UpdateForm_employee
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re

def index(request):
    return render(request ,'index.html')

def login(request):
    if request.method == "POST":
        username=request.POST['username']  
        password=request.POST['password']  
        role = request.POST.get('role')
        user=auth.authenticate(username=username,password=password)  
        
        if user is not None:
            auth.login(request,user)           
            return employer_dashboard(request) 
            
        else: 
            messages.info(request,'Credentials Invalid')
            return redirect('login')        
        
    return render(request,"login.html")

def signup(request):
    if request.method == "POST":
        username=request.POST['username']  
        password=request.POST['password']  
        password2=request.POST['password2'] 
        phone_pattern = re.compile(r'^\d{10}$')

        if not phone_pattern.match(username):
            messages.info(request, "Username must be a 10-digit phone number.")
            return redirect('signup')
        
        if password==password2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request,"username Taken")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username, password=password)
                user.save()
                user_login=auth.authenticate(username=username, password=password)
                auth.login(request,user_login)
                return redirect("/login")
        else:
            messages.info(request,'Password Not Matching')
            return redirect('signup') 
    else:
        return render(request, "signup.html")


@login_required(login_url='login')
def employer_dashboard(request):
    tasks = Task.objects.filter(employer=request.user)
    employees = Employee.objects.all() 
    return render(request, 'employer_dashboard.html', {'tasks': tasks, 'employees': employees})

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
    
 