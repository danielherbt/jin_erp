from django.contrib import admin

from api.manage.models import City, Company, Country, District, State, SubDistrict, Subsidiary

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(District)
admin.site.register(SubDistrict)
admin.site.register(Company)
admin.site.register(Subsidiary)
