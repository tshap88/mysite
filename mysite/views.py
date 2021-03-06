from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.
#from app1.models import App1,Choice
from recaptcha.client import captcha
from mysite import settings
from mysite.forms import ContactForm
from news.models import News, Article


def index(request):
    news = News.objects.all()
    news_mn = news.order_by('-date_pub')
    context = {'news_mn': news_mn}
    return render(request, 'index.html', context)

def articles(request):
    articles = Article.objects.all().order_by('-date_pub')
    context = {'articles' : articles}
    return render(request, 'articles.html', context)

def about(request):
    context = {'about': about}
    return render(request, 'about.html', context)

def thanks(request):
    context = {'thanks': thanks}
    return render(request, 'thanks.html', context)

def contact(request):
    captcha_error = ""
    captcha_pub_key = settings.RECAPTCHA_PUBLIC_KEY
    if request.method == 'POST':
        form = ContactForm(request.POST)
        cp_response = captcha.submit(request.POST.get("recaptcha_challenge_field", None),
                                         request.POST.get("recaptcha_response_field", None),
                                         settings.RECAPTCHA_PRIVATE_KEY,
                                         request.META.get("REMOTE_ADDR", None))

        if not cp_response.is_valid:
            captcha_error = "&error=%s" % cp_response.error_code
        else:
            if form.is_valid():
              cd = form.cleaned_data
              send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['tshap88@gmail.com'],
              )
              return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form,'captcha_error': captcha_error, 'captcha_pub_key': captcha_pub_key})
