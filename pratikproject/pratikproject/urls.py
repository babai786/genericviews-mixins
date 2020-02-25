"""pratikproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from pratikapp import views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('employeeget/',views.EmployeeList.as_view()),
    path('employeepost/',views.EmployeePost.as_view()),
    path('employeegetpost/',views.EmployeeListCreate.as_view()),
    path('employeeretrieve/<int:pk>/',views.EmployeeRetrieve.as_view()),
    path('employeeupdate/<int:id>/',views.EmployeeUpdate.as_view()),
    path('employeedelete/<int:id>/',views.EmployeeDestroy.as_view()),
    path('employeeretrieveupdate/<int:id>/', views.Employeeretrieveupdate.as_view()),
    path('employeeretrieveupdatedestroy/<int:id>/', views.Employeeretrieveupdatedestroy.as_view()),
    path('EmployeeListCreateModelMixin/',views.EmployeeListCreateModelMixin.as_view()),
    path('EmployeeRetrieveUpdateDestroyModelMixin/<int:pk>/',views.EmployeeRetrieveUpdateDestroyModelMixin.as_view()),

]


















