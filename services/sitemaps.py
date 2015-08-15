from django.contrib.sitemaps import Sitemap
from services.models import Service

class ServiceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Service.objects.all()