#-*- coding:utf-8 -*-
from django.contrib import admin
from bookhub import models as bookhub_model


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ('cover_img', 'title', 'douban_id', 'url_amazon')
    fields = ('title', ('cover', 'cover_img'), 'douban_id', 'url_amazon', 'desc')
    readonly_fields = ('cover_img', )

    def cover_img(self, ins):
        return '<img src="%s" title="%s"/>' % (ins.cover.url_100x150, ins.title)

    cover_img.short_description = "cover Preview"
    cover_img.allow_tags = True


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('book', 'chap_no', 'name', 'abstract')


admin.site.register(bookhub_model.Chapter, ChapterAdmin)
admin.site.register(bookhub_model.BookInfo, BookInfoAdmin)
