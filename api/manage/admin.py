from django.contrib import admin
from api.base.models import Genre
from api.manage.models import City, Company, Country, District, State, SubDistrict, Subsidiary, Modules, ConnectDb,UsersDb

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(District)
admin.site.register(SubDistrict)
admin.site.register(Company)
admin.site.register(Subsidiary)
admin.site.register(Modules)
admin.site.register(ConnectDb)
admin.site.register(Genre)
admin.site.register(UsersDb)