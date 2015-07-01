# -*- coding: utf-8-*-
from django.db import models

import datetime

from bookhub import models as bookhub_model
from django.contrib.auth.models import User


class ChapterLog(models.Model):
    reader = models.ForeignKey(User)

    book = models.ForeignKey(bookhub_model.BookInfo)
    chapter = models.ForeignKey(bookhub_model.Chapter)

    # TODO: 改为 tag, ManyToMany
    goal = models.TextField(u'阅读目的',
        help_text=u'打发时间? 有明确学习目的? 好玩好奇? 其他?',
        max_length=500, blank=True)
    feel = models.TextField(u'读后心情',
        help_text=u'达到最初阅读目的了么? 如果可以重新再来, 还会选择阅读么?',
        max_length=500, blank=True)

    to_read = models.BooleanField(u'需再读', default=False)
    why_more = models.TextField(u'再读目的',
        help_text=u'为何需要再读? 除了理解不透彻, 是否有其他原因? 为什么理解不透彻, 理论不足, 实践不足',
        max_length=500, blank=True)

    key_point = models.TextField(u'要点',
        help_text=u'作者论述的核心思路',
        max_length=500, blank=True)
    inspiration = models.TextField(u'感悟',
        help_text=u'自己对作者核心思路的理解与批评',
        max_length=500, blank=True)
    excerpt = models.TextField(u'摘录',
        help_text=u'主旨之外的精彩语句, 亮点',
        max_length=500, blank=True)

    timestamp = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return u'%s-%s' % (self.reader, self.chapter)

    class Meta:
        ordering = ['book', 'chapter', '-timestamp']
