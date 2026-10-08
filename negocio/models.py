from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.TextField()
    monto = models.PositiveIntegerField()
    boletos = models.BooleanField(default=True)

    class Meta:
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

    

class PaqueteTuristico(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    idavuelta = models.BooleanField()
    monto = models.PositiveIntegerField()
    destino = models.ForeignKey(
        Destino,
        on_delete=models.PROTECT,
        related_name='PaqueteTuristico'
    )
    
    def __str__(self):
        return self.nombre

