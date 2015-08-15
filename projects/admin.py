from django.contrib import admin
from .models import Project, Technology

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('Date', 'url', 'title', 'slug')
	list_filter = ('technologys', 'Date')
	search_fields = ('title',)
	list_editable = ('title', 'url', 'slug')
	filter_horizontal = ('categorys', 'technologys')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology)
