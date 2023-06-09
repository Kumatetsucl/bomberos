from django.db import models

class Comuna(models.Model):
    idComuna = models.AutoField(primary_key=True, verbose_name='Id comuna')
    nombre = models.CharField(max_length=50, verbose_name='Nombre comuna')

    def __str__(self):
        return self.nombre

class Cuartel(models.Model):
    idCuartel = models.AutoField(primary_key=True, verbose_name='ID')
    nombre = models.CharField(max_length=100, verbose_name='Nombre cuartel')
    direccion = models.CharField(max_length=100, null=True, blank=True, verbose_name='Direccion')
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Carro(models.Model):
    idCarro = models.AutoField(primary_key=True, verbose_name='ID Carro')
    patente = models.CharField(max_length=6, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca')
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name='Modelo')
    anno = models.IntegerField(verbose_name='Año')
    capacidadPersonas = models.IntegerField(verbose_name='Capacidad personas')
    capacidadLitros = models.IntegerField(verbose_name='Capacidad Litros')
    cuartel = models.ForeignKey(Cuartel, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.patente
    
class Cargo(models.Model):
    idCargo = models.AutoField(primary_key=True, verbose_name='ID Cargo')
    nombre = models.CharField(max_length=50, verbose_name='Nombre cargo')
    
    def __str__(self):
        return self.nombre

class Bombero(models.Model):
    idBombero = models.AutoField(primary_key=True, verbose_name='ID Bombero')
    rut = models.IntegerField(verbose_name='Rut')
    dv = models.CharField(max_length=1, verbose_name='Digito verificador')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apPaterno = models.CharField(max_length=50, verbose_name='Apellido paterno')
    apMaterno = models.CharField(max_length=50, verbose_name='Apellido materno')
    edad = models.IntegerField(verbose_name='Edad')
    telefono = models.IntegerField(verbose_name='Telefono')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    cuartel = models.ForeignKey(Cuartel, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nombre
    
class TipoEmergencia(models.Model):
    idTipoEmergencia = models.AutoField(primary_key=True, verbose_name='ID Tipo emergencia')
    nombre = models.CharField(max_length=50, verbose_name='Nombre emergencia')
    
    def __str__(self):
        return self.nombre
    
class Emergencia(models.Model):
    idEmergencia = models.AutoField(primary_key=True, verbose_name='ID Emergencia')
    tipo = models.ForeignKey(TipoEmergencia,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500, verbose_name='Descripcion')
    fechaInicio = models.DateField(verbose_name='Fecha inicio')

ESTADOS_HIDRANTE = (
    ('bueno', 'Bueno'),
    ('danado', 'Dañado'),
    ('falta_mantencion', 'Falta de Mantención'),
) 
 
class Hidrante(models.Model):
    

    idHidrante = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, choices=ESTADOS_HIDRANTE)


    def __str__(self):
        return f'Hidrante {self.idHidrante}: {self.direccion}'   
    
class ReporteFalla(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    hidrante = models.ForeignKey(Hidrante, on_delete=models.CASCADE, null=True)
    estado_hidrante = models.CharField(max_length=100, choices=ESTADOS_HIDRANTE, null=True)
    direccion = models.CharField(max_length=200)
    comentario = models.TextField()
    foto = models.ImageField(upload_to='fallas/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado_aprobado = models.BooleanField(default=False)
    
class Donacion(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    cuartel = models.ForeignKey(Cuartel, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
   
