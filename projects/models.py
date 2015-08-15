from django.db import models
from blog.models import Category

class Technology(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:		
		verbose_name_plural = 'Tecnologías'

class Project(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	image = models.ImageField(upload_to='projects/')
	url = models.CharField(max_length=100)
	num_slide = models.CharField(max_length=2)
	categorys = models.ManyToManyField(Category)
	technologys = models.ManyToManyField(Technology)
	Date = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(max_length=255, blank=True)

	def __str__(self):
		return self.title

	class Meta:		
		verbose_name_plural = 'Proyectos'

	def get_absolute_url(self):
		return '/proyectos/%s/' % self.slug
