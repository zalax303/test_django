#coding:utf-8
from django.conf.urls import url

urlpatterns = [
	url(r'^list/(?P<block_id>\d+)', "article.views.article_list", name="article_list"),
	#把\d匹配的数字都传递给block_id这个变量
	]

