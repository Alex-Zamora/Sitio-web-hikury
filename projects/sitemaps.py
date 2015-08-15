from django.contrib.sitemaps import Sitemap
from projects.models import Project

class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8 

    def items(self):
        return Project.objects.all()