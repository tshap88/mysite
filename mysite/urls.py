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
    url(r'^articles/$', views.articles, name = 'articles'),
    url(r'^about_us/$', views.about, name = 'about'),
    url(r'^blog/$', views.blog, name = 'blog'),
    url(r'^contact/$', views.contact, name = 'contact'),
    url(r'^contact/thanks/$', views.thanks, name='thanks'),
    url(r'^news/', include('news.urls', namespace = 'news')),

)
#handler404 = 'news.views.custom_404'
#handler500 = 'news.views.custom_500'
#handler400 = 'news.views.custom_400'
#handler403 = 'news.views.custom_403'

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
