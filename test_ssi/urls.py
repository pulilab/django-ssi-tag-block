from django.conf.urls import patterns, include, url
from django.shortcuts import render_to_response

import os
from django.conf import settings

def base_template(request):
    return {
        'included_template': os.path.abspath(os.path.join(settings.PROJECT_DIR, 'templates', 'ssi.html'))
    }

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', lambda r: render_to_response('page.html', base_template(r))),
    # url(r'^$', 'test_ssi.views.home', name='home'),
    # url(r'^test_ssi/', include('test_ssi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
