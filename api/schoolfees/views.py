#from rest_framework.decorators import action
from api.base.views import *
from api.base.serializers.entitiesSerializers import *
from api.base.serializers.personsSerializers import *
from api.base.serializers.dependSerializers import *
from api.base.serializers.docsSerializers import *

class InstitutionViewSet(BaseTypeViewSet):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()


class StudentViewSet(BaseTypeViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class PeriodViewSet(BaseTypeViewSet):
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()   


class CareerViewSet(BaseTypeViewSet):
    serializer_class = CareerSerializer
    queryset = Career.objects.all()


class LevelViewSet(BaseTypeViewSet):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()
  

class ParallelViewSet(BaseTypeViewSet):
    serializer_class = ParallelSerializer
    queryset = Parallel.objects.all()

    ###Sobreescribir el obtener un periodo
    # @action(detail=True, methods=['post','get','patch'],url_path='code')
    # def get_for_code(self,pk):
    #     parallel = Parallel.objects.filter(pk=id)
    #     return parallel

class KindViewSet(BaseTypeViewSet):
    serializer_class = KindSerializer
    queryset = Kind.objects.all()


class DebtViewSet(BaseViewSet):
    serializer_class = DebtSerializer
    queryset = Debt.objects.all()


class PaymentViewSet(BaseViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

#    def perform_create(self, serializer):
#        serializer.save(debt=self.request.debt_pay)
