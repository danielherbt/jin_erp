from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularJSONAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView
from drf_spectacular.views import SpectacularYAMLAPIView
from django.contrib import admin
from rest_framework import permissions
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Open API 자체를 조회 : json, yaml, 
    path("docs/json/", SpectacularJSONAPIView.as_view(), name="schema-json"),
    path("docs/yaml/", SpectacularYAMLAPIView.as_view(), name="swagger-yaml"),
    # Open API Document UI로 조회: Swagger, Redoc
    path("docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema-json"), name="swagger-ui",),
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="schema-json"), name="redoc",),

    path('api/administracion/', include('api.manage.urls')),
    path('api/escuelacobros/', include('api.schoolfees.urls')),
    path('api/ventas/', include('api.sales.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)