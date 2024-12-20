from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet, EmployeeViewSet, TaskViewSet
from . import views

router = DefaultRouter()
router.register(r'auth', AuthViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'task', TaskViewSet)


urlpatterns = [
    path('',include(router.urls),name="index"),
    path('login/<int:id>/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
        
    path('add-task/', views.add_task, name='add_task'),
    path('task_list', views.task_list, name='add_task'),
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>/', views.delete_selected_tasks, name='delete_employee'),    
    
    path('add_employee/', views.add_employee, name='add_employee'),
    path('employee_list', views.employee_list, name='add_task'),
    path('update_employee/<int:id>', views.update_employee, name='update'),  
    path('delete_employee/<int:id>/', views.delete_selected_employee, name='delete_employee'),  


]