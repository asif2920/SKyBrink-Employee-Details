from django.shortcuts import render, redirect
from .models import Employee


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializer import EmployeeSerializer

# Create your views here.
def insertform(request):
    context = {}
    return render(request, 'insertform.html', context)

def insert(request):
    emp = Employee()
    emp.firstname = request.POST['fname']
    emp.lastname = request.POST['lname']
    emp.designation = request.POST['designation']
    emp.department = request.POST['department']
    emp.employeeid = request.POST['emp_id']
    emp.save()
    #return render(request, 'loginsuccess.html',{'success':'Successfully inserted'})
    return redirect('getall')

def getall(request):
    employee1 = Employee.objects.all()
    serializer = EmployeeSerializer(employee1, many=True)
    context = {"data": serializer.data}
    return render(request, 'loginsuccess.html', context)

def updateform(request):
    context = {}
    return render(request,'updateform.html', context)

def updatecheck(request):
    emp = Employee.objects.get(employeeid = request.POST['eid'])
    if emp is not None:
        context = {
            'employeeid': emp.employeeid,
            'fname': emp.firstname,
            'lname':emp.lastname,
            'desig': emp.designation,
            'dept': emp.department
        }
        return render(request, 'updatecheckform.html', context)
    else:
        return render(request, 'updateform.html', {'error':'Emplyee id doesnot exist'})

def update(request):
    emp = Employee.objects.get(employeeid=request.POST['emp_id'])
    emp.firstname = request.POST['fname']
    emp.lastname = request.POST['lname']
    emp.designation = request.POST['designation']
    emp.department = request.POST['department']
    emp.employeeid = request.POST['emp_id']
    emp.save()
    return redirect('getall')


def deleteform(request):
    context = {}
    return render(request, 'deleteform.html', context)

def deletecheck(request):
    emp = Employee.objects.get(employeeid=request.POST['eid'])
    if emp is not None:
        context = {
            'employeeid': emp.employeeid,
            'fname': emp.firstname,
            'lname':emp.lastname,
            'desig': emp.designation,
            'dept': emp.department
        }
        return render(request, 'deletecheckform.html', context)
    else:
        return render(request, 'deleteform.html', {'error':'Emplyee id doesnot exist'})

def delete(request):
    emp = Employee.objects.get(employeeid=request.POST['emp_id'])
    return redirect('getall')

