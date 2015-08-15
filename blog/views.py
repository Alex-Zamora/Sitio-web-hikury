from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Post

def blog_view(request):
	posts = Post.objects.all().order_by('-id')

	paginator = Paginator(posts,4)

	try: 
		pagina = int(request.GET.get('page','1')) #liena importante
	except ValueError: pagina = 1

	try: 
		posts = paginator.page(pagina) #liena importante
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)

	return render(request, 'blog.html', {'posts':posts})

def blog_view_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog_detail.html', {'post':post})
