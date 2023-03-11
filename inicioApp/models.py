from django.db import models
# Create your models here.

class Trabajador(models.Model):
    id = models.AutoField(primary_key=True,)
    ci = models.CharField(max_length=10)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    estado = models.ImageField(default=True)
    class Meta: db_table='Trabajador'

class Usuario(models.Model):
    id = models.AutoField(primary_key=True,)
class Usuario(models.Model):
    id = models.AutoField(primary_key=True, )
    _id_trabajador_id=models.ForeignKey(Trabajador,on_delete=models.CASCADE)
    usuario= models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    estado= models.ImageField()
    id_trabajador = models.CharField(max_length=255)
    class Meta: db_table = 'Usuario'

