from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^campanha/', include('anjo.campaign.urls', namespace='campaign')),
    # Examples:
    # url(r'^$', 'anjo.views.home', name='home'),
    # url(r'^anjo/', include('anjo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('anjo.core.urls', namespace='home')),
)

from django.conf import settings
urlpatterns += patterns('django.views.static',
	url(r'^static/(?P<path>.*)$', 'serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^js/(?P<path>.*)$', 'serve', {'document_root': 'public/js'}),
)