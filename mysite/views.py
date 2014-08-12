from django.utils import timezone
from django.shortcuts import render
import datetime

# Create your views here.
#from app1.models import App1,Choice
from news.models import News

def index(request):
    now = datetime.datetime.now()
    news = News.objects.all()
    news_bar = News.objects.all().order_by('date_pub')[len(news)-1:len(news):-1]
    news_mn = News.objects.all().order_by('-date_pub') #[:len(news):-1]#[::-1] #only today
    context = {'news_bar': news_bar,
                'news_mn': news_mn
    }
    return render(request, 'index.html', context)


def support(request):
    news = News.objects.all()
    news_bar = news.order_by('date_pub')#[len(news)-5:len(news):-1]
    context = {'news_bar': news_bar}
    return render(request, 'support.html', context)


def about(request):
    news = News.objects.all()
    news_bar = news.order_by('date_pub')#[len(news)-5:len(news):-1]
    context = {'news_bar': news_bar}
    return render(request, 'about.html', context)


def blog(request):
    news = News.objects.all()
    news_bar = news.order_by('date_pub')#[len(news)-5:len(news):-1]
    context = {'news_bar': news_bar}
    return render(request, 'blog.html', context)


def contact(request):
    news = News.objects.all()
    news_bar = news.order_by('date_pub')[len(news)-5:len(news):-1]
    context = {'news_bar': news_bar}
    return render(request, 'contact.html', context)
