from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.schoolfees import views
from api.sales.views import ClientViewSet



# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'institucion', views.InstitutionViewSet)
router.register(r'representantes',ClientViewSet)
router.register(r'estudiantes', views.StudentViewSet)
router.register(r'periodos', views.PeriodViewSet)
router.register(r'carreras', views.CareerViewSet)
router.register(r'niveles', views.LevelViewSet)
router.register(r'paralelos', views.ParallelViewSet)
router.register(r'tipos', views.KindViewSet)
router.register(r'deudas', views.DebtViewSet)
router.register(r'pagos', views.PaymentViewSet)

urlpatterns = [
    path('', include(router.urls))
]