from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.listEmployee, name='list'),
    path('add/',views.addEmployee, name='add'),
    path('remove/', views.removeEmployee, name='remove'),
    path('remove/<int:emp_id>', views.removeEmployee, name='remove'),
   
]
