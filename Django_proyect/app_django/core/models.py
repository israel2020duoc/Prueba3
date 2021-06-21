from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoría')

    def __str__ (self):
        return self.nombreCategoria


class Libro(models.Model):
    isbn = models.CharField(max_length=12, primary_key=True, verbose_name='ISBN')
    nombre_libro = models.CharField(max_length=40, verbose_name='Nombre libro')
    autor = models.CharField(max_length=40, verbose_name='Autor')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField( max_length=400, verbose_name='Descripción')
    
    def __str__(self):
        return self.nombre_libro

