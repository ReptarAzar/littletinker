from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from littletinker import settings

admin.autodiscover()

urlpatterns = patterns('web.views',
    url(r'^$', 'home'),
    url(r'^about/$', 'about'),
    url(r'^projects/$', 'projects'),
    url(r'^project/(\d+)$', 'one_project'),
    url(r'^labs/(.+)$', 'labs'),
    url(r'^jobs/$', direct_to_template, {'template': 'jobs.html'}),
    url(r'^contact/', 'contact_us'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )