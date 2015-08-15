from django.contrib.sitemaps import Sitemap
from blog.models import Post

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Post.objects.all()