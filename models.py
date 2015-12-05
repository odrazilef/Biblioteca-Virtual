
#biblioteca/models.py
from django.db import models

# Create your models here.
class Editor(models.Model):
    '''Un editor tiene un nombre, un domicilio, una ciudad, un estado, un pais y un sitio web'''
    nombre = models.CharField(max_length=30)#el atributo nombre tendra maximo 30 caracteres
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)#el atributo pais tendra maximo 50 caracteres
    website = models.URLField()
    #....
	  class Meta:
        verbose_name_plural = 'Editores'

    def __unicode__(self):#__str__ para python 3
        return self.nombre
#______________________________________________________________________         
class Autor(models.Model):
    '''Un autor tiene un nombre, un apellido y un email'''
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(blank=True)#La BBDD aceptara valores vacios para este atributo
     #....
	    class Meta:
        verbose_name_plural = 'Autores'
    def __unicode__(self):#__str__ para python 3
        cadena = "%s %s" %(self.nombre, self.apellido)
        return cadena 
#______________________________________________________________________
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor)
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to = 'portadas/')#Crea una carpeta llamada portadas, donde guardara las imagenes de portadas de libros, al final la imagen tendra que cargarse en: media/portadas/, eso lo veremos luego
    sinopsis = models.TextField(blank=True)
    
    def __unicode__(self):#__str__ para python 3
        return self.titulo
