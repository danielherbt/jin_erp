from django.urls import include,path
from rest_framework.routers import DefaultRouter
from api.manage import views
from api.manage.views import ConnectDbViewSet, ModulesViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'pais', views.CountryViewSet)
router.register(r'provincia', views.StateViewSet)
router.register(r'ciudad', views.CityViewSet)
router.register(r'parroquia', views.DistrictViewSet)
router.register(r'subparroquia', views.SubDistrictViewSet)
router.register(r'compania', views.CompanyViewSet)
router.register(r'sucursal', views.SubsidiaryViewSet)
router.register(r'genero',views.GenreViewSet)
router.register(r'conexion-bd', ConnectDbViewSet)
router.register(r'modulo', ModulesViewSet)

urlpatterns = [
    path('', include(router.urls))
]