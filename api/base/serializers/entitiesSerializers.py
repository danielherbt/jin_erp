from rest_framework import serializers
from api.manage.models import Country, State, City, District, SubDistrict ,Company ,Subsidiary
from api.schoolfees.models import Institution

###----------- Manage ---------------------------------
class CountrySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Country
        exclude = ('status','created','updated')
 
class StateSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = State
        exclude = ('status','created','updated')

class CitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = City
        exclude = ('status','created','updated')

class DistrictSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = District
        exclude = ('status','created','updated')

class SubDistrictSerializer(serializers.HyperlinkedModelSerializer):
 
    class Meta:
        model = SubDistrict
        exclude = ('status','created','updated')

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # state = serializers.BooleanField(style={'input-type':'checkbox'})

    class Meta:
        model = Company
        ref_name = "Empresa"
        exclude = ('status','created','updated')    

class SubsidiarySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Subsidiary
        exclude = ('status','created','updated')

###----------- School Fees ---------------------------------
class InstitutionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Institution
        exclude = ('status','created','updated')




