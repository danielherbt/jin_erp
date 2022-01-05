from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions,viewsets
from rest_framework import filters
from api.base.pagination import ExtendedPagination

class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

     # Sistema de paginación
    pagination_class = ExtendedPagination

    class Meta:
        """Meta definition for BaseModel."""
        abstract = True

class BaseEntityViewSet(BaseViewSet):
    # # Sistema de filtros
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
    #'year': ['lte', 'gte'],  # Año menor o igual, mayor o igual que
    'dni' : ['exact'],      # Código exacto
    'name' : ['contains']
    }
    search_fields = ['name','dni','id']
    ordering_fields = ['name','dni','id']

  
class BaseTypeViewSet(BaseViewSet):
# # Sistema de filtros
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
    #'year': ['lte', 'gte'],  # Año menor o igual, mayor o igual que
    'code' : ['exact'],      # Código exacto
    'name' : ['contains']
    }
    search_fields = ['name','code','id']
    ordering_fields = ['name','code','id']
