from django.db import models

class ProjectConstruccion(models.Model):
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField()
	link = models.CharField(max_length=200, blank=True)
	imagen = models.ImageField(upload_to='construccion/')
	fecha = models.DateField(null=True, blank=True)
	status = models.BooleanField(default=True)

	def __str__(self):
		return self.titulo

	class Meta:		
		verbose_name_plural = 'En construccion'
