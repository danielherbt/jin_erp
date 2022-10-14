from rest_framework import serializers
from api.schoolfees.models import Debt, Payment
from api.docs.models import Agreements, Docs #, ClassDocs


###-----------Exclusiv School Fees-------------------
class DebtSerializer(serializers.HyperlinkedModelSerializer):
  
    class Meta:
        model = Debt
        fields = '__all__'
    
    def to_representation(self,instance):
        data = super().to_representation(instance)
        
        return {
                'url' : data['url'],
                'id'     : instance.id,
                'Fecha de Deuda': instance.date,
                'Código de Deuda' : instance.code,
                'Valor de Deuda' : instance.value,
                'Estudiante' : instance.student.name,
                'Estudiante Url': data['student'],
                'Carrera' : instance.career.name,
                'Carrera Url': data['career'],
                'Nivel' : instance.level.name,
                'Nivel Url': data['level'],
                'Tipo' : instance.kind.name,
                'Tipo Url': data['kind'],
                'Periodo' : instance.period.name,
                'Periodo Url': data['period'],
                'Paralelo' : instance.parallel.name,
                'Paralelo Url': data['parallel'],
                'Institucion' : instance.institut.name,
                'Institucion Url' : data['institut']
        }    

class PaymentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
        #exclude = ['code_pay']

    def to_representation(self,instance):
        data = super().to_representation(instance)
    
        return {
            'url' : data['url'],
            'id'     : instance.id,
            'Fecha de Pago': instance.date,
            'Código de Pago' : instance.code,
            'Valor de Pago' : instance.value,
            'Deuda Código' : instance.debt.code,
            'Deuda Url': data['debt'],
            'Cliente' : instance.client.name,
            'Clinte Url' : data['client']
        } 

###-----------Exclusiv Docs---------------------------
class DocSerializer(serializers.HyperlinkedModelSerializer):
    ### Para que se muestre el nombre del campo relacionado en lugar del ID
    #classdoc = serializers.SlugRelatedField(slug_field="name", queryset=ClassDocs.objects.all())
    class Meta:
        model = Docs
       # exclude = ('status','created','updated')  
        fields = '__all__'

class AgreeDocSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agreements
        # exclude = ('status','created','updated') 
        fields = '__all__'