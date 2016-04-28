#coding:utf-8
from django.contrib import admin

from models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("title", "block", "owner", "create_time", "update_time")
	search_fields = ["title", "content"]  #外键字段不能够被搜索
	list_filter = ("block", )

admin.site.register(Article, ArticleAdmin)
