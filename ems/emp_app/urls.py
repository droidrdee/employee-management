from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('list', views.listEmployee),
    path('add',views.addEmployee),
    path('delete', views.removeEmployee),
    path('search', views.searchEmployee),
]
