from rest_framework  import serializers
from pratikapp.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    # def validate_esal(self,value):
    #     if value<2000:
    #         raise serializers.ValidationError('SALARY IS TOO LOW')
    #     return  value
    #
    # def validate(self,data):
    #     ename=data.get('ename')
    #     esal=data.get('esal')
    #     if ename.lower()=='babai':
    #         if esal<100000:
    #             raise serializers.ValidationError('SALARY SHOULD BE HIGH')
    #     return data
    class Meta:
        model= Employee
        fields= '__all__'
