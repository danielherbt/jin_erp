from datetime import datetime
from django.db import models
from api.base.models import TypesBaseModel, EntityBaseModel
from api.manage.models import Company, Modules

class ClassDocs(TypesBaseModel):
    sri = models.BooleanField(verbose_name='SRI',help_text='Si es un documento para el SRI')

    class Meta:
        """Meta definition for BaseModel."""
        verbose_name = 'Tipo Documento'
        verbose_name_plural = 'Tipos Documentos'
        ordering = ['name']

    def __str__(self):
        return self.name    

class Docs(TypesBaseModel):
    classdoc = models.ForeignKey(ClassDocs, verbose_name='TipoDoc', help_text='Tipo de Documento',on_delete=models.RESTRICT)
    
    datedoc = models.DateField(verbose_name='Fecha',help_text='Fecha del documento',blank=True,null=True)
    pathxmldoc = models.CharField(verbose_name='Ruta 1',help_text='Ruta donde se guarda el archivo 1',max_length=255,blank=True,null=True)
    pathpdfdoc = models.CharField(verbose_name='Ruta 2',help_text='Ruta donde se guarda el archivo 2',max_length=255,blank=True,null=True)
    receiverdoc = models.CharField(verbose_name='Destinatario',help_text='Persona que recibe el documento',max_length=100,blank=True,null=True)
    rucdoc = models.CharField(verbose_name='Ruc',help_text='Ruc del receptor del Documento',max_length=13,blank=True,null=True)
    xmldoc = models.FileField('Xml',help_text='Documento Xml',upload_to='XML/', max_length=255,blank=True,null=True)
    pdfdoc = models.FileField('Pdf',help_text='Documento Pdf',upload_to='PDF/', max_length=255, blank=True,null=True)
    access   = models.CharField(verbose_name='Acceso',help_text='Clave de Acceso para el SRI',max_length=49,blank=True,null=True)
    serie = models.CharField(verbose_name='Serie',help_text='Serie del documento para el SRI',max_length=7,blank=True,null=True)
    number = models.PositiveIntegerField(verbose_name='Número',help_text='Numeración del Documento',blank=True,null=True)
   
    class Meta:
        """Meta definition for BaseModel."""
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['name']

    def __str__(self):
        return self.name

class Agreements(TypesBaseModel):
    classdoc = models.ForeignKey(ClassDocs, verbose_name='TipoDoc', help_text='Tipo de Documento',on_delete=models.RESTRICT)
    company = models.ForeignKey(Company, verbose_name='Empresa', help_text='Empresa que tiene el servicio',on_delete=models.RESTRICT)
    module = models.ForeignKey(Modules, verbose_name='Modulo', help_text='Modulo disponible en el Acuerdo',on_delete=models.RESTRICT)

    contact = models.CharField(verbose_name='Contacto',help_text='Persona de Contacto',max_length=100,blank=True,null=True)
    chargcontac = models.CharField(verbose_name='Cargo',help_text='Cargo del Contacto',max_length=50,blank=True,null=True)
    start = models.DateTimeField(verbose_name='Inicio',help_text='Fecha de Inicio del Contrato',default=datetime.now,blank=False)
    end = models.DateTimeField(verbose_name='Finalizacion',help_text='Fecha de Finalización del Contrato',blank=False)
    comment = models.CharField(verbose_name='Comentarios',help_text='Comentarios del Acuerdo',max_length=255,blank=True,null=True)
    monthly = models.BooleanField(verbose_name='Mensual',help_text='Si es un valor mensual')
    valueunit = models.DecimalField(max_digits=10,decimal_places=2,help_text='Valor de servicio',verbose_name='Valor Unitario',blank=False,null=False)

    class Meta:
        """Meta definition for BaseModel."""
        verbose_name = 'Cláusula'
        verbose_name_plural = 'Cláusulas'
        ordering = ['name']

    def __str__(self):
        return self.name
