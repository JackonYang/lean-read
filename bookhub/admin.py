#-*- coding:utf-8 -*-
from django.contrib import admin
from bookhub import models as bookhub_model


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'douban_id', 'url_amazon')


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('book', 'chap_no', 'name', 'abstract')


admin.site.register(bookhub_model.Chapter, ChapterAdmin)
admin.site.register(bookhub_model.BookInfo, BookInfoAdmin)
