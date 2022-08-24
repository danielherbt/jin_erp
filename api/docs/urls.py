from django.urls import include,path
from rest_framework.routers import DefaultRouter
from api.docs import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tipo-documento', views.ClassDocViewSet)
router.register(r'documento', views.DocsViewSet)
router.register(r'acuerdo', views.AgreeViewSet)

urlpatterns = [
    path('', include(router.urls))
]