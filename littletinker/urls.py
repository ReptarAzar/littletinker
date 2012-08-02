from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from littletinker import settings
from web.models import Project
from django.contrib.sitemaps import Sitemap, FlatPageSitemap
from django.contrib.flatpages.models import Flatpage

admin.autodiscover()

class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.date

flatpage_dict = {
    'queryset': Flatpage.objects.all(),
}

sitemaps = {
    'flatpages': GenericSitemap(flatpage_dict, priority=0.8),
    'projects': ProjectSitemap,
}

urlpatterns = patterns('web.views',
    url(r'^$', direct_to_template, {'template':'index.html'}),
    url(r'^about/$', direct_to_template, {'template':'about.html'}),
    url(r'^about/(.+)/$', 'about'),
    url(r'^projects/$', direct_to_template, {'template':'projects.html'}),
    url(r'^project/(\d+)$', 'one_project'),
    url(r'^jobs/$', direct_to_template, {'template': 'jobs.html'}),
    url(r'^contact/', 'contact_us'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# le sitemap
urlpatterns += patterns('',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

if settings.DEBUG and settings.DEPLOYED is False:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )