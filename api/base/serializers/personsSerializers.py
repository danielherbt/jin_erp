from rest_framework import serializers
from api.sales.models import Client,Vendor
from api.schoolfees.models import Student

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        exclude = ('status','created','updated')


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        exclude = ('status','created','updated')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        #fields = '__all__'
        exclude = ('status','created','updated') 