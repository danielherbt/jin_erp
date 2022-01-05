from rest_framework import serializers
from api.base.models import Genre
from api.schoolfees.models import Period, Career, Level, Parallel, Kind



class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        exclude = ('status','created','updated')

###-----------Exclusiv School Fees-------------------

class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Period
        exclude = ('status','created','updated')
        
class CareerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Career
        exclude = ('status','created','updated')

class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        exclude = ('status','created','updated')

class ParallelSerializer(serializers.HyperlinkedModelSerializer):
    # state = serializers.BooleanField(style={'input-type':'checkbox'})
    class Meta:
        model = Parallel
        exclude = ('status','created','updated')   

class KindSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kind
        exclude = ('status','created','updated')
###---------------------------------------------------------
