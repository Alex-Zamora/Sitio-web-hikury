from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from blog.sitemaps import PostSitemap
from projects.sitemaps import ProjectSitemap
from services.sitemaps import ServiceSitemap

sitemaps = {
    'blog': PostSitemap(), 'proyectos': ProjectSitemap(), 'servicios':ServiceSitemap()
}


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.home_view', name='home'),
    url(r'^servicios/(?P<slug>[\w\-]+)/', 'services.views.service_detail_view', name='service_detail'),
    url(r'^servicios/', 'services.views.service_view_all', name='service_view_all'),
    url(r'^proyectos/', 'projects.views.project_view', name='project_view'),
    url(r'^blog/(?P<slug>[\w\-]+)/', 'blog.views.blog_view_detail', name='blog_detail'),
    url(r'^blog/', 'blog.views.blog_view', name='blog_view'),
    url(r'^contacto/', 'contact.views.contact_view', name='contacto'),
    url(r'^proyectos-en-desarrollo/', 'construccion.views.ConstruccionView', name='en_desarrollo'),
    #Usiarios
    url(r'^nuevo-usuario/', 'usuarios.views.nuevo_usuario', name='nuevo_usuario'),
    url(r'^iniciar-sesion/', 'usuarios.views.iniciar_sesion', name='iniciar-sesion'),
    url(r'^cerrar-sesion/', 'usuarios.views.cerrar_sesion', name='cerrar-sesion'),
    (r'^summernote/', include('django_summernote.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^robots.txt$', include('robots.urls')),

)