#-*- coding:utf-8 -*-
from django.db import models


class BookInfo(models.Model):
    title = models.CharField(u'Title', max_length=100)
    desc = models.TextField(u'desc', max_length=500, blank=True)
    douban_id = models.CharField(u'Douban ID', max_length=100)
    url_amazon = models.CharField(u'Amazon URL', max_length=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Book Infos'


class Chapter(models.Model):
    book = models.ForeignKey(BookInfo)
    chap_no = models.IntegerField(u'ChapNo.')
    name = models.CharField(u'name', max_length=100)
    abstract = models.TextField(u'abstract desc', max_length=500, blank=True)

    def __unicode__(self):
        return u'%s-Chap %s.%s' % (self.book.title, self.chap_no, self.name)
