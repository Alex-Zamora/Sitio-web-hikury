from django.contrib import admin
from .models import Service
from django_summernote.admin import SummernoteModelAdmin

class ServiceAdmin(SummernoteModelAdmin):
	list_display = ('icon','title', 'slug')
	list_editable = ('title','slug')

admin.site.register(Service, ServiceAdmin)
