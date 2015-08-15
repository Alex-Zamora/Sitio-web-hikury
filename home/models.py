from django.db import models

class Home(models.Model):
	image_index = models.ImageField(upload_to='home/')
	title_index = models.CharField(max_length=100)
	logo_menu = models.ImageField(upload_to='home/')
	telephone = models.CharField(max_length=50)
	movil = models.CharField(max_length=50)
	email = models.EmailField(max_length=80)

	def __str__(self):
		return self.title_index

	class Meta:		
		verbose_name_plural = 'Home'
