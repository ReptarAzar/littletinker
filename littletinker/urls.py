from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from littletinker import settings
from django.contrib.sitemaps import Sitemap

admin.autodiscover()

class tinkerSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

urlpatterns = patterns('web.views',
    url(r'^$', 'home'),
    url(r'^about/$', 'about'),
    url(r'^about/(.+)/$', 'about'),
    url(r'^hacks/$', 'about'),
    url(r'^projects/$', 'projects'),
    url(r'^project/(\d+)$', 'one_project'),
    url(r'^project/git$', 'labs', {'projectNameRequest':'git'}),
    url(r'^project/instatinker', 'labs', {'projectNameRequest':'instatinker'}),
    url(r'^jobs/$', direct_to_template, {'template': 'jobs.html'}),
    url(r'^contact/', 'contact_us'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # le sitemap
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': tinkerSitemap})

)

if settings.DEBUG and settings.DEPLOYED is False:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )