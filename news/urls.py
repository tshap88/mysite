from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('',
    url(r'^$', views.NewsAll, name='NewsAll'),
    url(r'^(?P<ar_slug>.*)/$', views.SingleNews, name='SingleNews'),

)

