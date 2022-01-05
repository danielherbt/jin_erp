from django.db import models
from api.base.models import Commercial

class Vendor(Commercial): 
    commision = models.DecimalField(verbose_name='Comisión', max_digits=5, decimal_places=2,blank=True,null=True,help_text='Porcentaje de Comisión')  
    collecter = models.BooleanField(verbose_name='Cobrador',help_text='Si es cobrador también')

    class Meta:
        ordering = ['name']
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.name

class Client(Commercial):   

    vendor = models.ForeignKey(Vendor, verbose_name='Vendedor', help_text='Seleccione un vendedor', on_delete=models.RESTRICT)

    class Meta:
        ordering = ['name']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name   
