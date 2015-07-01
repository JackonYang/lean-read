# -*- coding: utf-8-*-
from django.contrib import admin
from leanread import models as leanread_model


class ChapterLogAdmin(admin.ModelAdmin):
    list_display = ('book', 'chapter', 'reader', 'goal', 'feel', 'to_read')


admin.site.register(leanread_model.ChapterLog, ChapterLogAdmin)
