from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

PHONE_NUMBER_REGEX = RegexValidator(r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$', 'Se requiere un teléfono válido')
DNI_NUMBER_REGEX = RegexValidator(r'^[A-Za-z0-9]{10,13}','Letras o números solamente')

### Main Model for all others.
class BaseModel(models.Model):
    """Model definition for BaseModel."""

    # TODO: Define fields here
    status = models.BooleanField(verbose_name ='Activo',default = 1)
    created = models.DateTimeField(verbose_name ="Creado",help_text ='Fecha de Creación', auto_now=False, auto_now_add=True, editable=False)
    updated = models.DateTimeField(verbose_name ="Modificado",help_text='Fecha de Modificación', auto_now=True, auto_now_add=False, editable=False)
    #deleted_date = models.DateField('Fecha de Eliminación', auto_now=True, auto_now_add=False)
    historical = HistoricalRecords(user_model=User, inherit=True)
   
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'

### Class abstract for inherit from here for models with only one field :description
### Use for lists of selecction

class TypesBaseModel(BaseModel):
    name = models.CharField(verbose_name='Nombre', max_length=100,help_text='Descripción',blank=False,null=False,unique=True)
    code = models.CharField(verbose_name='Código', max_length=50,help_text='Código Único',unique=True,blank=True,null=True)

    class Meta:
        """Meta definition for BaseModel for Types."""
        abstract = True
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['name']

    def __str__(self):
        return self.name

class Genre(TypesBaseModel):

    juridic = models.BooleanField(verbose_name='Jurídica',help_text='Si es persona jurídica', default=False)

    class Meta:
        """Meta definition for BaseModel."""
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

    def __str__(self):
        return self.name

### Object Person

class EntityBaseModel(BaseModel):
    """Model definition for EntityBaseModel."""
    genre = models.ForeignKey(Genre, verbose_name='Género',help_text='Tipo o Género', on_delete=models.RESTRICT,related_name='+')
    
    dni = models.CharField(max_length=13, verbose_name="Identificación",help_text="Número de Identificación", unique = True,validators=[DNI_NUMBER_REGEX])
    name = models.CharField(max_length=100, verbose_name="Nombre",help_text="Nombre o Razón Social",blank=False,null=False)
    lastname = models.CharField(max_length=100, verbose_name="Segundo Nombre",help_text="Apellido o Nombre Comercial",blank=True,null=True)
    birth = models.DateField(verbose_name="Natalicio",help_text="Fecha de Cumpleaños", auto_now=False, auto_now_add=False,blank=True,null=True)
    email = models.EmailField(verbose_name='Correo Electrónico',max_length = 255, unique = True)
    photo = models.ImageField( upload_to='img', height_field=None, width_field=None, max_length=255, verbose_name="Imagen",help_text="Foto o Imagen en formato png",blank=True,null=True)
    comment = models.TextField(verbose_name="Observaciones",help_text="Información Adicional",default=None,blank=True,null=True)
    
    class Meta:
        """Meta definition for EntityBaseModel."""
        abstract = True
        verbose_name = 'Modelo Base Persona'
        verbose_name_plural = 'Modelos Base Personas'


class BaseLocation(TypesBaseModel):
    #subdistrict = models.ForeignKey(SubDistrict, verbose_name='Subparroquia', on_delete=models.RESTRICT,help_text='En que subparroquia esta ubicada')
    
    ref = models.TextField(verbose_name='Referencias',help_text='Información Adicional',null=True,blank=True)
    lon = models.CharField(verbose_name='Longitud', max_length=50,help_text='Coordenadas de Longitud',blank=True,null=True)
    lat = models.CharField(verbose_name='Latitud', max_length=50,help_text='Coordenadas de Latitud',blank=True,null=True)
    postal = models.CharField(verbose_name='Postal', max_length=50,null=True,blank=True,help_text='Número del Código Postal')

    class Meta:
            """Meta definition for BaseModel."""
            verbose_name = 'Location'
            verbose_name_plural = 'Locations'
            abstract = True


class Address(BaseLocation):
    class TypeAddress(models.TextChoices):
        HOME ='P','Personal'
        WORK ='W','Laboral'
        OTHERS ='O','Otro'

    kind = models.CharField(verbose_name='Tipo', max_length=1, help_text='Tipo de Teléfono',choices=TypeAddress.choices,default='HOME')
    secondary = models.CharField(verbose_name='Calle Secundaria', max_length=100,null=True,blank=True)
    number = models.CharField(verbose_name='Numeración', max_length=10,null=True,blank=True,help_text='Numeración de la dirección')
    current = models.BooleanField(verbose_name='Actual',help_text='Si es la direción actual')

    class Meta:
            """Meta definition for BaseModel."""
            verbose_name = 'Dirección'
            verbose_name_plural = 'Direcciones'
            abstract = True

 
class Phones(BaseModel):
    class TypePhone(models.TextChoices):
        MOVIL = 'M','Celular'
        LANDLINE = 'L','Fijo'
        OTHER = 'O','Otro'

    phone = models.CharField('Teléfono',max_length=14,blank=True,default='',null=True,help_text="Telefono Ej:+(593)-99809-4322 ",validators=[PHONE_NUMBER_REGEX])
    principal = models.BooleanField(verbose_name='Principal',help_text='Si es el teléfono principal')
    kind = models.CharField(verbose_name='Tipo', max_length=1, help_text='Tipo de Teléfono',choices=TypePhone.choices,default='MOVIL')
    use = models.CharField(verbose_name='Uso', max_length=1, help_text='Tipo de Uso del Teléfono',choices=Address.TypeAddress.choices,default='HOME')
    ext = models.CharField(verbose_name='Extensión', max_length=10,null=True,blank=True,help_text='Extensión del Número de Teléfono')
    
    class Meta:
            """Meta definition for BaseModel."""
            verbose_name = 'Teléfono'
            verbose_name_plural = 'Teléfonos'  
            abstract = True  
   
           
### Models inherit of Person
class Commercial(EntityBaseModel):
    term = models.IntegerField(help_text='Plazo de Crédito en dias',verbose_name='Plazo',default=0)
    percent_discount = models.DecimalField(max_digits=5,decimal_places=2,help_text='Porcentaje de Descuento',verbose_name='Descuento',default=0)
    #serie = models.CharField(verbose_name='Serie',help_text='Número de Serie SRI',max_length=7,blank=True,null=True,validators=[SERIE_NUMBER_REGEX])

    class Meta:
        """Meta definition for EntityBaseModel."""
        abstract = True
        verbose_name = 'Base Persona Comercial'
        verbose_name_plural = 'Base Personas Comercial'            
        
               