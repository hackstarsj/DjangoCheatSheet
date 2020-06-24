"""DjangoCheatSheet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from DjangoCheatSheetApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo_response',views.demoResponse,name="demoresponse"),
    path('insert_data',views.insert_data,name="insert_data"),
    path('save_insert_data',views.save_insert_data,name="save_insert_data"),
    path('read_all_employee',views.read_all_employee,name="read_all_employee"),
    path('edit_employee/<str:id>',views.edit_employee,name="edit_employee"),
    path('save_edit_data',views.save_edit_data,name="save_edit_data"),
    path('delete_employee/<str:id>',views.delete_employee,name="delete_employee"),
    path('login_user',views.login_user,name="login_user"),
    path('login_user_post',views.login_user_post,name="login_user_post"),
    path('logout_user',views.logout_user,name="logout_user"),
    path('protected_page',views.protected_page,name="protected_page"),
]
