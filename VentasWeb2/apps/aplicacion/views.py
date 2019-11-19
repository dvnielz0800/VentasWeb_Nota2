from django.shortcuts import render,redirect
from .models import *
from .forms import ClienteForm
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

def home(request):
	return render(request,'aplicacion/index.html')

def inicio(request):
	return render(request,'aplicacion/inicio.html')	


class CreateCliente(CreateView):
	model = Cliente 
	form_class = ClienteForm
	template_name = 'aplicacion/crear_cliente.html'
	success_url = reverse_lazy('index') 

class ListCliente(ListView):
	model = Cliente 
	template_name = 'aplicacion/listar_cliente.html'
	
class UpdateCliente(UpdateView):
	model = Cliente 
	form_class = ClienteForm
	template_name = 'aplicacion/crear_cliente.html'
	success_url = reverse_lazy('index') 

class DeleteCliente(DeleteView):
	model = Cliente 
	template_name = 'aplicacion/eliminar_cliente.html'
	success_url = reverse_lazy('index') 





































def CrearCliente(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = ClienteForm()
	return render(request,'aplicacion/crear_cliente.html', {'form':form})

def listarCliente(request):
	cliente = Cliente.objects.all()
	context = {'cliente':cliente}	
	return render(request,'aplicacion/listar_cliente.html',context)	

def editarCliente(request,Rut):
	cliente = Cliente.objects.get(Rut = Rut)
	if request.method == 'GET':
		form = ClienteForm(instance = cliente)
	else:
		form = ClienteForm(request.POST, instance = cliente)
		if form.is_valid():
			form.save()
		return redirect('index')	
	return render(request,'aplicacion/crear_cliente.html',{'form':form})	

def eliminarCliente(request,Rut):
	cliente = Cliente.objects.get(Rut = Rut)
	if request.method == 'POST':
		cliente.delete()
		return redirect('index')
	return render(request,'aplicacion/eliminar_cliente.html',{'cliente':cliente})




		




