# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'news_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('date_pub', self.gf('django.db.models.fields.DateTimeField')()),
            ('contents', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('img_file', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('img_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'news', ['Article'])

        # Deleting field 'News.news_article'
        db.delete_column(u'news_news', 'news_article')


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'news_article')

        # Adding field 'News.news_article'
        db.add_column(u'news_news', 'news_article',
                      self.gf('django.db.models.fields.CharField')(default='foo', max_length=50),
                      keep_default=False)


    models = {
        u'news.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'contents': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_pub': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'img_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['news']