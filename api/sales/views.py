from api.base.views import BaseEntityViewSet
from api.base.serializers.personsSerializers import *

class VendorViewSet(BaseEntityViewSet):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()

class ClientViewSet(BaseEntityViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
