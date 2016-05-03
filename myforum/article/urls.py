#coding:utf-8
from django.conf.urls import url

urlpatterns = [
	url(r'^lists/(?P<block_id>\d+)', "article.views.article_list", name="article_list"),
	#把\d匹配的数字都传递给block_id这个变量
	url(r'^create/(?P<block_id>\d+)', "article.views.create_article", name="create_article"),
	]

