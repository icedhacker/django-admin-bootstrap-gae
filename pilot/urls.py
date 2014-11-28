"""
URL configuration.
"""

from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()

# pylint: disable=C0103
urlpatterns = patterns(
    '',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include(admin.site.urls), name='home'),
)
