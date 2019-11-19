from django.db import models

# Create your models here.

class Marca(models.Model):
	NombreMarca = models.CharField(max_length=30)

	def __str__(self):
		return  self.NombreMarca

class TipoRopa(models.Model):
	TipoRopa = models.CharField(max_length=30)

	def __str__(self):
		return  self.TipoRopa

class Producto(models.Model):
	id = models.AutoField(primary_key= True)
	Nombre = models.CharField(max_length=50)	
	Modelo = models.CharField(max_length=50)
	Color = models.CharField(max_length=20)
	GENERO = (('M','Masculino'), ('F','Femenino'), ('U','Unisex'))
	Genero = models.CharField(max_length=1, choices=GENERO, default='M')
	TipoRopa = models.ForeignKey(TipoRopa, null=False, blank=False, on_delete=models.CASCADE)
	Marca = models.ForeignKey(Marca, null=False, blank=False, on_delete=models.CASCADE)
	FechaCreacion = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		cadena = "{0} / {1}"
		return cadena.format(self.TipoRopa ,self.Nombre)

class Cliente(models.Model):
	Nombre_Completo = models.CharField(max_length=50)
	Correo_Electronico = models.EmailField()
	Rut = models.IntegerField(primary_key=True, max_length=8)
	Telefono = models.IntegerField(max_length=10)

	def __str__(self):
		cadena = "{0} / {1}"
		return cadena.format(self.Rut ,self.Nombre_Completo)


