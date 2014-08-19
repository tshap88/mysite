from django.shortcuts import render, get_object_or_404, render_to_response
from news.models import News

def Last5News(request):
    news = News.objects.all().order_by('date_pub')[:5]
    context = {'news': news}
    return render(request, 'index.html','support.html','about.html','blog.html','contact.html',context)

def NewsAll(request):
    news = News.objects.all().order_by('-date_pub')
    context = {'news': news}
    return render(request, 'news/news.html',context)

def SingleNews(request, ar_slug):
    news = get_object_or_404(News, slug = ar_slug)
    context = {'news': news}
    return render(request, 'news/singlenews.html',context)


def custom_400(request):
    return render_to_response('400.html')

def custom_403(request):
    return render_to_response('403.html')

def custom_404(request):
    return render_to_response('404.html')

def custom_500(request):
    return render_to_response('500.html')