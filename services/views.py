from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Service


def service_detail_view(request, slug):

	service = get_object_or_404(Service, slug = slug)

	return render(request, 'service_detail.html', {'service':service})


def service_view_all(request):

	services = Service.objects.all().order_by('-id')[:4]

	return render(request, 'services.html', {'services':services})