from django.shortcuts import render, HttpResponse, redirect
from .models import Employee, Role, Department
from datetime import datetime

def index(request):
    return render(request, 'base.html')



def listEmployee(request):
    emp = Employee.objects.all()
    emplist = {
        'emp':emp
    }
   
    return render(request, 'list.html', emplist)


def addEmployee(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        salary = int(request.POST['salary'])
        depart = int(request.POST['dept'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        addemp = Employee(first_name=firstname, last_name=lastname, salary=salary, dept_id=depart, role_id=role, phone=phone, join_date=datetime.now())
        addemp.save()
        return redirect('add.html')
    
    elif request.method == 'GET':
        return render(request, 'add.html')
    else:
        return HttpResponse('Error occured')
        



def removeEmployee(request, emp_id = 0):
    if emp_id:
        try:
            emp_removed = Employee.objects.get(id=emp_id)
            emp_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please select A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove.html',context)