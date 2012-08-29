from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from littletinker import settings
from web.models import Project
from django.contrib.sitemaps import Sitemap, GenericSitemap
from django.contrib.flatpages.models import FlatPage
from web.forms import ContactForm

admin.autodiscover()

class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.date

class HomeSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.00

    def items(self):
        home = [{'name':"home", 'location':'/'},{'name':"about", 'location':'/projects'}]
        return home

    def location(self, obj):
        return obj['location']

class AboutSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        home = [{'name':"about", 'location':'/about'},{'name':"team", 'location':'/about/team'},{'name':"process", 'location':'/about/process'}]
        return home

    def location(self, obj):
        return obj['location']

flatpage_dict = {
    'queryset': FlatPage.objects.all(),
}

sitemaps = {
    'home': HomeSitemap,
    'about': AboutSitemap,
    'flatpages': GenericSitemap(flatpage_dict, priority=0.3),
    'projects': ProjectSitemap,
}

urlpatterns = patterns('web.views',
    url(r'^$', 'home'),
    url(r'^about/$', direct_to_template, {'template':'about.html', 'extra_context': {'form': ContactForm(initial={'message': 'Message'})}}),
    url(r'^about/(.+)/$', 'about'),
    url(r'^projects/$', direct_to_template, {'template':'projects.html', 'extra_context': {'form': ContactForm(initial={'message': 'Message'})}}),
    url(r'^project/(\d+)$', 'one_project'),
    url(r'^jobs/$', direct_to_template, {'template': 'jobs.html', 'extra_context': {'form': ContactForm(initial={'message': 'Message'})}}),
    url(r'^contact/', 'contact_us'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# le sitemap, le robots.txt, and le humans.txt
urlpatterns += patterns('',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    (r'^humans\.txt$', direct_to_template, {'template': 'humans.txt', 'mimetype': 'text/plain'}),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),
)

if settings.DEBUG and settings.DEPLOYED is False:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )
