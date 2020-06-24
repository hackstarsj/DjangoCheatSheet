from django.contrib import admin

# Register your models here.
from DjangoCheatSheetApp.models import Designation, EmployeeData

admin.site.register(Designation)
admin.site.register(EmployeeData)