from django.conf.urls import patterns, url

from news import views


urlpatterns = patterns('',
    url(r'^article/(?P<article_slug>.*)/$', views.SingleArticle, name='SingleArticle'),
    url(r'^(?P<news_slug>.*)/$', views.SingleNews, name='SingleNews'),


)

