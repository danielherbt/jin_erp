from django.urls import include,path
from rest_framework.routers import DefaultRouter
from api.sales import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'vendedor', views.VendorViewSet)
router.register(r'cliente', views.ClientViewSet)

urlpatterns = [
    path('', include(router.urls))
]