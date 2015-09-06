from django.shortcuts import render
from .models import ProjectConstruccion
from django.contrib.auth.decorators import login_required

@login_required(login_url='/iniciar-sesion/')
def ConstruccionView(request):
	
	proyecto = ProjectConstruccion.objects.all()

	return render(request, 'construccion.html', {'proyectos': proyecto})
