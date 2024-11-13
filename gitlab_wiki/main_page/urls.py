from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name="index"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
        
    path('add-task/', views.add_task, name='add_task'),
    path('task_list', views.task_list, name='add_task'),
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>/', views.delete_selected_tasks, name='delete_employee'),    
    
    path('add_employee/', views.add_employee, name='add_employee'),
    path('employee_list', views.employee_list, name='add_task'),
    path('update_employee/<int:id>', views.update_employee, name='update'),  
    path('delete_employee/<int:id>/', views.delete_selected_employee, name='delete_employee'),  


]