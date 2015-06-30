# -*- coding: utf-8-*-
from django.contrib import admin
from leanread import models as leanread_model


class ChapterLogAdmin(admin.ModelAdmin):
    list_display = ('chapter', 'reader', 'comment', 'timestamp')


admin.site.register(leanread_model.ChapterLog, ChapterLogAdmin)
