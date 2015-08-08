from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hikury.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.home_view', name='home'),
    url(r'^servicios/(?P<slug>[\w\-]+)/', 'services.views.service_detail_view', name='service_detail'),
    url(r'^servicios/', 'services.views.service_view_all', name='service_view_all'),
    url(r'^proyectos/', 'projects.views.project_view', name='project_view'),
    url(r'^blog/(?P<slug>[\w\-]+)/', 'blog.views.blog_view_detail', name='blog_detail'),
    url(r'^blog/', 'blog.views.blog_view', name='blog_view'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),


)