from django import template
from projects.models import Project

register = template.Library()

@register.inclusion_tag('projects.html', takes_context=True)
def show_projects(context):
	projects = Project.objects.all()

	return {'MEDIA_URL': context['MEDIA_URL'], 'projects':projects}