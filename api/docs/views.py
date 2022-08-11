from api.base.views import BaseEntityViewSet, BaseTypeViewSet
from api.base.serializers.entitiesSerializers import *
from api.base.serializers.dependSerializers import *
from api.base.serializers.docsSerializers import *


class DocsViewSet(BaseTypeViewSet):
    serializer_class = DocSerializer
    queryset = Docs.objects.all()

class ClassDocViewSet(BaseTypeViewSet):
    serializer_class = ClassDocSerializer
    queryset = ClassDocs.objects.all()    

class AgreeViewSet(BaseTypeViewSet):
    serializer_class = AgreeDocSerializer
    queryset = Agreements.objects.all()  