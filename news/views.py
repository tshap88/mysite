from django.shortcuts import render, get_object_or_404, render_to_response
from news.models import News, Article

def Last5News(request):
    news = News.objects.all().order_by('date_pub')[:5]
    context = {'news': news}
    return render(request, 'index.html','articles.html','about.html','contact.html',context)

def NewsAll(request):
    news = News.objects.all().order_by('-date_pub')
    context = {'news': news}
    return render(request, 'news/news.html',context)

def SingleNews(request, news_slug):
    news = get_object_or_404(News, slug = news_slug)
    context = {'news': news}
    return render(request, 'news/singlenews.html',context)

def SingleArticle(request, article_slug):
    article = get_object_or_404(Article, slug = article_slug)
    context = {'article': article}
    return render(request, 'news/singlearticle.html',context)


#def custom_400(request):
#    return render_to_response('400.html')

#def custom_403(request):
#    return render_to_response('403.html')

#def custom_404(request):
#    return render_to_response('404.html')

#def custom_500(request):
#    return render_to_response('500.html')