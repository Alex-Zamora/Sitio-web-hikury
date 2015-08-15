from django.contrib import admin
from .models import Category, Post
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
	list_display = ('date', 'title', 'slug','user')
	list_filter = ('category', 'date')
	search_fields = ('title',)
	list_editable = ('title','slug','user')
	filter_horizontal = ('category',)

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
