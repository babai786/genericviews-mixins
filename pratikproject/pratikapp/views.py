from django.shortcuts import render

# Create your views here.
from pratikapp.serializers import EmployeeSerializer
from rest_framework import  serializers
from pratikapp.models import  Employee
from rest_framework.generics import ListAPIView,ListCreateAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,\
    RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
import json
import requests
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated





class EmployeeList(ListAPIView):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer



class EmployeeRetrieve(RetrieveAPIView):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer
    #lookup_field = 'id'


class EmployeeUpdate(UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field='id'


class EmployeeDestroy(DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field='id'



class Employeeretrieveupdate(RetrieveUpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field='id'


class Employeeretrieveupdatedestroy(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field='id'


class EmployeePost(CreateAPIView):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer



class EmployeeListCreate(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



##########################  MIXINS  #####################################

from rest_framework import mixins


class EmployeeListCreateModelMixin(mixins.CreateModelMixin,ListAPIView):
    queryset=Employee.objects.all()
    serializer_class =  EmployeeSerializer
    #lookup_field = 'id'
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)



class EmployeeRetrieveUpdateDestroyModelMixin(mixins.DestroyModelMixin,mixins.UpdateModelMixin,RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
















