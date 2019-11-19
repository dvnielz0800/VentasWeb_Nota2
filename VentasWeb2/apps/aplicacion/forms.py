from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = [
		'Nombre_Completo',
		'Correo_Electronico',
		'Rut',
		'Telefono',
		]