from django.conf.urls import patterns, include, url
import task.views as res

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    # url(r'^todo/', include('todo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', res.Index()),
    url(r'^tasks$', res.Tasks()),
    url(r'^tasks/(\d+)$', res.Task()),
)

import settings
if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': settings.STATIC_ROOT
			}),
	)