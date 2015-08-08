from django import template
from services.models import Service

register = template.Library()

@register.inclusion_tag('services.html', takes_context=True)
def show_services(context):
	services = Service.objects.all().order_by('id')[:4]

	return {'MEDIA_URL': context['MEDIA_URL'], 'services':services }