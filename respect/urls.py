from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from mezzanine.conf import settings


admin.autodiscover()

# Serve static media during development so things look right
if settings.DEBUG:
    urlpatterns = patterns(
        '',
        (r'^{0}/(?P<path>.*)$'.format(settings.MEDIA_URL.strip('/')),
         'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

urlpatterns += i18n_patterns(
    "",
    ("^admin/", include(admin.site.urls)))

urlpatterns += patterns(
    '',
    url("^$", "mezzanine.pages.views.page", {"slug": "/"}, name="home"),
    ("^", include("mezzanine.urls")))

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
