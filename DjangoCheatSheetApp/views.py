from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from DjangoCheatSheetApp.models import Designation, EmployeeData


def demoResponse(request):
    return HttpResponse("Demo Data")

def insert_data(request):
    designation=Designation.objects.all()
    return render(request,"insert_data.html",{"designation":designation})

def save_insert_data(request):
    if request.method!="POST":
        messages.error(request,"Only POST Method is Allowed")
        return HttpResponseRedirect(reverse("insert_data"))
    else:
        name=request.POST.get("employee_name")
        employee_age=request.POST.get("employee_age")
        employee_address=request.POST.get("employee_address")
        employee_email=request.POST.get("employee_email")
        designation=request.POST.get("designation")

        try:
            designation_object=Designation.objects.get(id=designation)
            employee=EmployeeData(name=name,age=employee_age,email=employee_email,address=employee_address,designation=designation_object)
            employee.save()
            messages.success(request, "Data Saved Successfully")
            return HttpResponseRedirect(reverse("insert_data"))
        except:
            messages.error(request, "Error in Saving Data")
            return HttpResponseRedirect(reverse("insert_data"))

def read_all_employee(request):
    employees=EmployeeData.objects.all()
    total_employees=employees.count()
    return render(request,"read_all_employee.html",{"employees":employees,"total_employees":total_employees})

def edit_employee(request,id):
    employee=EmployeeData.objects.get(id=id)
    designation=Designation.objects.all()
    return render(request,"edit_employee.html",{"employee":employee,"designation":designation})

def save_edit_data(request):
    id=request.POST.get("id")
    name=request.POST.get("name")
    email=request.POST.get("email")
    age=request.POST.get("age")
    designation=request.POST.get("designation")
    address=request.POST.get("address")

    try:
        designation_obj=Designation.objects.get(id=designation)
        employee=EmployeeData.objects.get(id=id)
        employee.name=name
        employee.email=email
        employee.age=age
        employee.address=address
        employee.designation=designation_obj
        employee.save()
        messages.success(request, "Data Saved Successfully")
        return HttpResponseRedirect(reverse("edit_employee",kwargs={"id":id}))
    except:
        messages.error(request, "Error in Saving Data")
        return HttpResponseRedirect(reverse("edit_employee",kwargs={"id":id}))

def delete_employee(request,id):
    employee=EmployeeData.objects.get(id=id)
    employee.delete()
    messages.success(request, "Data Deleted Successfully")
    return HttpResponseRedirect(reverse("read_all_employee"))

def login_user(request):
    return render(request,"login_user.html")

def login_user_post(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(username=username,password=password)
    if user:
        if user!=None:
            login(request, user)
            return HttpResponse("Login Successfull")
        else:
            return HttpResponse("Invalid Login Details")
    else:
        return HttpResponse("Invalid Login Details")

def logout_user(request):
    logout(request)
    request.user=None
    return HttpResponseRedirect(reverse("login_user"))

@login_required(login_url="login_user")
def protected_page(request):
    return HttpResponse("This is Protected Page")