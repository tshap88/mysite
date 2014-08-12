from django.conf.urls import patterns, include, url
import views
from django.contrib import admin
from filebrowser.sites import site

admin.autodiscover()
urlpatterns = patterns('',

    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name = 'index'),
    url(r'^support/$', views.support, name = 'support'),
    url(r'^about_us/$', views.about, name = 'about'),
    url(r'^blog/$', views.blog, name = 'blog'),
    url(r'^contact/$', views.contact, name = 'contact'),
    url(r'^news/', include('news.urls', namespace = 'news')),

)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
