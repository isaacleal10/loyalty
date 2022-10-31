from django.db import models

class Contacto(models.Model):
    eIdentificacion = models.CharField(max_length=20)
    eNombre = models.CharField(max_length=100)
    eApellidos = models.CharField(max_length=100)
    eCorreo = models.EmailField()
    eTelefono = models.CharField(max_length=15)
    class Meta:
        db_table = "contacto"
