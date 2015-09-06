from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def nuevo_usuario(request):
	# Si el request trae metodo POST
	if request.method == 'POST':
		# Entonces se guardan los datos en la variable formulario
		formulario = UserCreationForm(request.POST)
		# Ahora se comprueba la informacion si es valida
		if formulario.is_valid():
			# Se guarda la informacion
			formulario.save()
			return HttpResponseRedirect('/')
	# Si el metodo es Get
	else:
		formulario = UserCreationForm()
	return render(request, 'new_user.html', {'formulario':formulario})

def iniciar_sesion(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/proyectos-en-desarrollo/')
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username = usuario, password = clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('proyectos-en-desarrollo')
				else:
					return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/')
	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form':form})


def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect('/proyectos-en-desarrollo/')
