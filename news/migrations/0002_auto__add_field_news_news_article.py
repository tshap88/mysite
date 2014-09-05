# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.news_article'
        db.add_column(u'news_news', 'news_article',
                      self.gf('django.db.models.fields.CharField')(default='news', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News.news_article'
        db.delete_column(u'news_news', 'news_article')


    models = {
        u'news.news': {
            'Meta': {'object_name': 'News'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'contents': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_pub': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'img_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'news_article': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['news']