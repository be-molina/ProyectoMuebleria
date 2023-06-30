from django.db import models

# Create your models here.


class Categoria_prod(models.Model): 
    id_categoria = models.AutoField(db_column='idCategoria', primary_key=True)
    categoria    = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)

class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=10)
    nombre_prod = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=100)
    precio      = models.IntegerField()
    #img_prod = models.BlobField(null=True, blank=True)
    stock = models.IntegerField()
    categoria_prod = models.ForeignKey('Categoria_prod', on_delete=models.CASCADE, db_column='')

    def __str__(self):
        return str(self.nombre_prod)+" "+str(self.precio)

class Boleta(models.Model):
        id_boleta = models.AutoField(db_column='idBoleta', primary_key=True)
        detalle_boleta = models.CharField(max_length=100)

        def __str__(self):
            return str(self.detalle_boleta)

class Usuario(models.Model):
    id_usuario = models.AutoField(db_column='idUsuario', primary_key=True)
    nombre_usuario     = models.CharField(max_length=30)
    apellido_paterno   = models.CharField(max_length=25)
    apellido_materno   = models.CharField(max_length=25)  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)
    boleta = models.ForeignKey('Boleta', on_delete=models.CASCADE, db_column='')

    def __str__(self):
        return str(self.nombre_usuario)+" "+str(self.boleta.detalle_boleta)



