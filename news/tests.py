from django.test import TestCase
from news.models import News
from django.utils import timezone

# Create your tests here.

class NewsMethodTests(TestCase):

    def setUp(self):

        News.objects.create(name='Aaa', slug='aaa', date_pub=timezone.now(), contents='a a a a a a', author='111',
                            link='https://docs.djangoproject.com/en/1.6/intro/tutorial01/', img_file='home/tania/PycharmProjects/VM/sites/media/imgs/count-link.png',
                            img_url='')
        News.objects.create(name='Bbb', slug='bbb', date_pub=timezone.now(), contents='b b b b b b', author='222',
                            link='https://docs.djangoproject.com/en/1.6/intro/tutorial02/', img_file='',
                            img_url='http://pds.exblog.jp/pds/1/201407/28/27/c0198227_21415628.jpg')
        News.objects.create(name='Ccc', slug='ccc', date_pub=timezone.now(), contents='c c c c c c', author='333',
                            link='https://docs.djangoproject.com/en/1.6/intro/tutorial03/', img_file='', img_url='')
        News.objects.create(name='Ddd', slug='ddd', date_pub=timezone.now(), contents='d d d d d d', author='444',
                            link='', img_file='', img_url='')
        News.objects.create(name='Eee', slug='eee', date_pub=timezone.now(), contents='', author='555',
                            link='', img_file='', img_url='')


    def test_news(self):

        Aaa_news = News.objects.get(name = 'Aaa')
        Bbb_news = News.objects.get(name = 'Bbb')
        Ccc_news = News.objects.get(name = 'Ccc')
        Ddd_news = News.objects.get(name = 'Ddd')
        Eee_news = News.objects.get(name = 'Eee')

        self.assertEqual(Aaa_news.img_file, 'home/tania/PycharmProjects/VM/sites/media/imgs/count-link.png')
        self.assertEqual(Bbb_news.img_url, 'http://pds.exblog.jp/pds/1/201407/28/27/c0198227_21415628.jpg')
        self.assertEqual(Ccc_news.name, 'Ccc')
        self.assertEqual(Ccc_news.link, 'https://docs.djangoproject.com/en/1.6/intro/tutorial03/')
        self.assertEqual(Ddd_news.slug, 'ddd')
        self.assertEqual(Ddd_news.contents, 'd d d d d d')
        self.assertEqual(Eee_news.author, '555')
