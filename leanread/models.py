# -*- coding: utf-8-*-
from django.db import models

import datetime

from bookhub.models import Chapter
from django.contrib.auth.models import User


class ChapterLog(models.Model):
    chapter = models.ForeignKey(Chapter)
    reader = models.ForeignKey(User)
    goal = models.TextField(u'Goal', max_length=500, blank=True)
    comment = models.TextField(u'Brief Comment', max_length=500, blank=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return u'%s-%s' % (self.reader, self.chapter)

    class Meta:
        ordering = ['chapter', '-timestamp']
