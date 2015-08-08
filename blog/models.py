from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class Post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	imagePrev = models.ImageField(upload_to='blog/')
	imagePost = models.ImageField(upload_to='blog/')
	category = models.ManyToManyField(Category)
	user = models.ForeignKey(User)
	slug = models.SlugField(max_length=200, blank=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


