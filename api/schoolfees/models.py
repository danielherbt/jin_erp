from datetime import datetime
from django.core.validators import RegexValidator
from django.db import models
from api.base.models import  BaseModel, TypesBaseModel
from api.sales.models import Client

PHONE_NUMBER_REGEX = RegexValidator(r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$', 'Se requiere un teléfono válido')
# ### otra forma ^[a-z0-9_-]{3,16}$ Empezamos diciendole al analizador sintáctico que encuentre el principio de la cadena (^), 
# # seguido de cualquier letra minúscula (a-z), número (0-9), un carácter de subrayado o un guión. 
# # A continuación, {3,16} asegura que sean al menos 3 de esos caracteres, 
# # pero no más de 16. Por último, queremos el final de la cadena ($).
# #DNI_NUMBER_REGEX = RegexValidator(r'^[a-z0-9]{1,13}$','Letras o números solamente')
# #DNI_NUMBER_REGEX = RegexValidator(r'^\w$','Letras o números solamente')

class Institution(TypesBaseModel):

    class Meta:
        ordering = ['name']
        verbose_name = 'Institución'
        verbose_name_plural = 'Instituciones'

    def __str__(self):
        return self.name

    #Para grabar en mayusuculas
    # def save(self, *args, **kwargs):
    #     self.DNI = (self.DNI).uppercase()
    #     self.Nombre = (self.Nombre).uppercase()
    #     self.Apellidos = (self.Apellidos).uppercase()
    #     return super(TuModelo, self).save(*args, **kwargs)
 

class Student(TypesBaseModel):
    address = models.CharField(max_length=254, verbose_name="Direccion",help_text="Casa",blank=True,null=True)
    phone = models.CharField(max_length=14, verbose_name="Teléfono",help_text="Celular o Convencional",blank=True,null=True,validators=[PHONE_NUMBER_REGEX])
    email = models.EmailField(verbose_name='Email',max_length = 255, unique = True,blank=True,null=True,help_text="Dirección de Correo Electrónico")
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return self.name
        #return f"{self.lastname} {self.name}"    

class Period(TypesBaseModel):

    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'

    def __str__(self):
        return self.name   

class Career(TypesBaseModel):
   
    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
    
    def __str__(self):
        return self.name   

class Level(TypesBaseModel):
    code = models.CharField(verbose_name='Código', max_length=50,help_text='Código',blank=True,null=True)

    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveles'  

    def __str__(self):
        return self.name   

class Parallel(TypesBaseModel):

    class Meta:
        verbose_name = 'Paralelo'
        verbose_name_plural = 'Paralelos'

    def __str__(self):
        return self.name

    """ def save(self, *args, **kwargs):
        self.name = (self.name).uppercase()
        return super(Parallel, self).save(*args, **kwargs)
  """

class Kind(TypesBaseModel):

    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies' 

    def __str__(self):
        return self.name

class Debt(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT,verbose_name='Estudiante',help_text='Seleccione el estudiante',blank=False,null=False)
    career = models.ForeignKey(Career, on_delete=models.RESTRICT,verbose_name='Carrera',help_text='Seleccione la carrera',blank=False,null=False)
    level = models.ForeignKey(Level, on_delete=models.RESTRICT,verbose_name='Nivel',help_text='Seleccione el nivel',blank=False,null=False)
    kind = models.ForeignKey(Kind, on_delete=models.RESTRICT,verbose_name='Especie',help_text='Seleccione la especie',blank=False,null=False)
    period = models.ForeignKey(Period, on_delete=models.RESTRICT,verbose_name='Periodo',help_text='Seleccione el periodo',blank=False,null=False)
    parallel = models.ForeignKey(Parallel, on_delete=models.RESTRICT,verbose_name='Paralelo',help_text='Seleccione el paralelo',blank=False,null=False)
    institut = models.ForeignKey(Institution, on_delete=models.RESTRICT,verbose_name='Institucion',help_text='A que institución pertenece',blank=False,null=False)

    code = models.CharField(max_length=50,verbose_name='Código',help_text='ID de otro sistema',unique=True,blank=False,null=False)
    date = models.DateTimeField(verbose_name='Fecha',help_text='Fecha del registro de deuda',default=datetime.now,blank=True,null=False)
    value = models.DecimalField(max_digits=10,decimal_places=2,help_text='Valor de la deuda',verbose_name='Valor',blank=False,null=False)
    
    class Meta:
        ordering = ['date']
        verbose_name = 'Deuda'
        verbose_name_plural = 'Deudas'

    def __str__(self):
        return self.code


class Payment(BaseModel):
    debt = models.ForeignKey(Debt, on_delete=models.RESTRICT,verbose_name='Deuda',blank=False,null=False,help_text='Seleccione el id de deuda')
    client = models.ForeignKey(Client, on_delete=models.RESTRICT,verbose_name='Representante',help_text='A nombre de quien sale la factura',blank=False,null=False)

    date = models.DateTimeField(verbose_name='Fecha de Pago',help_text='Fecha del Pago',default=datetime.now,blank=False)
    code = models.CharField(max_length=50,verbose_name='Código de Pago',help_text='Identificador ',blank=False,null=False)
    value = models.DecimalField(max_digits=10,decimal_places=2,help_text='Ingrese el valor del pago',verbose_name='Valor del Pago',blank=False,null=False)

    class Meta:
        ordering = ['date']
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
    
    def __str__(self):
        return self.code
        #return f"{self.code_pay} {self.first_name}"   
    