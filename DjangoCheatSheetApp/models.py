from django.db import models

# Create your models here.
class Designation(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    objects=models.Manager()

class EmployeeData(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default="")
    age=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100,default="")
    address=models.CharField(max_length=100,default="")
    designation=models.ForeignKey(Designation,max_length=100,on_delete=models.CASCADE)
    objects=models.Manager()