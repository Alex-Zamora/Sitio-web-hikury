from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_view(request):
	posts = Post.objects.all().order_by('-id')
	return render(request, 'blog.html', {'posts':posts})

def blog_view_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog_detail.html', {'post':post})
