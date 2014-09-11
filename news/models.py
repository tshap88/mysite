import urllib2
import urlparse
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField('slug')
    date_pub = models.DateTimeField('date published')
    contents = models.TextField(blank=True)
    author = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    img_file = models.ImageField('file name', upload_to='imgs_n/', blank=True)
    img_url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.img_url:
            image_data = urllib2.urlopen(self.img_url, timeout=5)
            filename = urlparse.urlparse(image_data.geturl()).path.split('/')[-1]
            self.img_file = filename
            self.img_file.save(
                filename,
                ContentFile(image_data.read()),
                save=False
            )
        super(News, self).save(*args, **kwargs)

    def delete(self, using=None):
        if self.img_file:
            @receiver(post_delete, sender=News)
            def news_post_delete_handler(sender, **kwargs):
                news = kwargs['instance']
                storage, path = news.img_file.storage, news.img_file.path
                storage.delete(path)

        super(News, self).delete()

class Article(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField('slug')
    date_pub = models.DateTimeField('date published')
    contents = models.TextField(blank=True)
    author = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    img_file = models.ImageField('file name', upload_to='imgs_a/', blank=True)
    img_url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.img_url:
            image_data = urllib2.urlopen(self.img_url, timeout=5)
            filename = urlparse.urlparse(image_data.geturl()).path.split('/')[-1]
            self.img_file = filename
            self.img_file.save(
                filename,
                ContentFile(image_data.read()),
                save=False
            )
        super(Article, self).save(*args, **kwargs)

    def delete(self, using=None):
        if self.img_file:
            @receiver(post_delete, sender=Article)
            def article_post_delete_handler(sender, **kwargs):
                article = kwargs['instance']
                storage, path = article.img_file.storage, article.img_file.path
                storage.delete(path)
        super(Article, self).delete()
