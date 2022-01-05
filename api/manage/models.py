from django.core.validators import RegexValidator
from django.db import models
from api.base.models import TypesBaseModel, EntityBaseModel

DNI_NUMBER_REGEX = RegexValidator(r'^[A-Za-z0-9]{10,13}','Letras o números solamente')
SERIE_NUMBER_REGEX = RegexValidator(r'^[0-9]{3}-[0-9]{3}','Debe tener el formato "###-###"')

#### Here Models with inherit only base and use in the multiples apps and other many models
### Country,City,States,District

class Country(TypesBaseModel):

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.name

class State(TypesBaseModel):
    country = models.ForeignKey(Country, verbose_name='País', on_delete=models.RESTRICT,help_text='En que país esta ubicado')

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return self.name        

class City(TypesBaseModel):
    state = models.ForeignKey(State, verbose_name='Provincia', on_delete=models.RESTRICT,help_text='En que provincia esta ubicada')

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.name        

class District(TypesBaseModel):
    city = models.ForeignKey(City, verbose_name='Ciudad', on_delete=models.RESTRICT,help_text='En que ciudad esta ubicada')

    class Meta:
        verbose_name = 'Parroquia'
        verbose_name_plural = 'Parroquias'

    def __str__(self):
        return self.name      


class SubDistrict(TypesBaseModel):
    district = models.ForeignKey(District, verbose_name='Parroquia', on_delete=models.RESTRICT,help_text='En que parroquia esta ubicada')

    class Meta:
        verbose_name = 'Subparroquia'
        verbose_name_plural = 'Subparroquias'

    def __str__(self):
        return self.name   


class Company(EntityBaseModel):
    agentret = models.BooleanField(verbose_name ='Retención',help_text="Si es agente de Retención")
    artisan = models.BooleanField(verbose_name ='Artesano',help_text="Si es artesano")
    micro = models.BooleanField(verbose_name ='Microempresa',help_text="Si es microempresa")
    electronic = models.BooleanField(verbose_name ='Electrónica',help_text="Si factura electrónicamente")
    account = models.BooleanField(verbose_name ='Contabilidad',help_text="Si es Obligado a llevar contabilidad")
    agent = models.CharField(verbose_name="Representante", max_length=255,)
    agentdni = models.CharField(verbose_name="Dni Representante", max_length=10,validators=[DNI_NUMBER_REGEX],help_text="Cédula del Representante Legal")
    accountant = models.CharField(verbose_name="Contador", max_length=255,)
    accountantdni = models.CharField(verbose_name="Dni Contador", max_length=13,validators=[DNI_NUMBER_REGEX],help_text="Ruc del Contador")

    class Meta:
        ordering = ['name']
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.name

class Subsidiary(EntityBaseModel):
    company = models.ForeignKey(Company, verbose_name='Compania', help_text='Compania a la que pertenece',on_delete=models.RESTRICT)
    matrix = models.BooleanField(verbose_name='Matriz',help_text='Si es la matriz')
    serie = models.CharField(verbose_name='Serie',help_text='Número de Serie SRI',max_length=7,blank=True,null=True,validators=[SERIE_NUMBER_REGEX])

    class Meta:
        """Meta definition for BaseModel."""
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
        ordering = ['name']

    def __str__(self):
        return self.name    
