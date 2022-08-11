from api.base.views import BaseEntityViewSet, BaseTypeViewSet
from api.base.serializers.entitiesSerializers import *
from api.base.serializers.dependSerializers import *
from api.base.serializers.personsSerializers import *


class CountryViewSet(BaseTypeViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class StateViewSet(BaseTypeViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()    


class CityViewSet(BaseTypeViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

class DistrictViewSet(BaseTypeViewSet):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()


class SubDistrictViewSet(BaseTypeViewSet):
    serializer_class = SubDistrictSerializer
    queryset = SubDistrict.objects.all()   

class CompanyViewSet(BaseEntityViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class SubsidiaryViewSet(BaseEntityViewSet):
    serializer_class = SubsidiarySerializer
    queryset = Subsidiary.objects.all()

class GenreViewSet(BaseTypeViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class UserDbViewSet(BaseTypeViewSet):
    serializer_class = UserDbSerializer
    queryset = UsersDb.objects.all()    

class ConnectDbViewSet(BaseTypeViewSet):
    serializer_class = ConnectDbSerializer
    queryset = ConnectDb.objects.all()     

class ModulesViewSet(BaseTypeViewSet):
    serializer_class = ModuleSerializer
    queryset = Modules.objects.all() 