from django.shortcuts import render
from .models import Project

def project_view(request):
 
	project = Project.objects.all()

	return render(request, 'projects.html', {'projects':project})
