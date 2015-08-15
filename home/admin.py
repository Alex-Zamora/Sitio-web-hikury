from django.contrib import admin
from .models import Home

class HomeAdmin(admin.ModelAdmin):
	list_display = ('logo_menu','title_index', 'telephone', 'movil', 'email')
	list_editable = ('title_index', 'telephone', 'movil', 'email')

admin.site.register(Home, HomeAdmin)
