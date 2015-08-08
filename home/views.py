from django.shortcuts import render
from django.http import HttpResponse
from .models import Home

def home_view(request):
	home = Home.objects.get(pk=1)
	return render(request, 'index.html', {'home':home})
