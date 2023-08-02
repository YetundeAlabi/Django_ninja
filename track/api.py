from typing import List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, UploadedFile, File

from .schema import EmployeeIn, EmployeeOut
from .models import Employee

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return "Hello World"

# @api.post("/employees")
# def create_employee(request, payload: EmployeeIn):
#     employee = Employee.objects.create(**EmployeeIn.dict())
#     return {"id": employee.id}


# handling file upload
@api.post("/employees")
def create_employees(request, payload: EmployeeIn, cv:UploadedFile = File(...)):
    payload_dict = payload.dict()
    employee = Employee(**payload_dict)
    employee.cv.save(cv.name, cv)
    return {"id": employee.id}

# retrieve single object
@api.get("/employees/{employee_id}", response=EmployeeOut)
def get_employee(request, employee_id: int):
    employee = get_object_or_404(Employee, employee_id)
    return employee


# list object
@api.get("/employees", response=List[EmployeeOut])
def list_employees(request):
    qs = Employee.objects.all()
    return qs

# update object
@api.put("/employees/{employee_id}")
def update_employees(request, employee_id: int, payload: EmployeeIn):
    employee = get_object_or_404(Employee, employee_id)
    for attr, value in payload.dict().items():
        setattr(employee, attr, value)
    employee.save()
    return {"success": True}

# delete object
@api.delete("/employees/{employee_id}")
def delete_employee(request, employee_id: int):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return {"success": True}