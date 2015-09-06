from django.contrib import admin
from .models import ProjectConstruccion

class ConstructionAdmin(admin.ModelAdmin):
	list_display = ('imagen', 'titulo', 'link', 'fecha', 'status')
	search_fields = ('titulo',)
	list_editable = ('titulo', 'link', 'fecha', 'status')

admin.site.register(ProjectConstruccion, ConstructionAdmin)