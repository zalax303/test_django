#coding:utf-8
from django.shortcuts import render_to_response

from block.models import Block
from models import Article


# Create your views here.
def article_list(request, block_id):  #block_id来自于url中的block_id变量
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)  #get方法要求只返回一个结果
	articles = Article.objects.filter(block=block).order_by("-update_time")
	#filter相当于sql where条件 -代表倒序
	return render_to_response("article_list.html", {"articles": articles, "block": block})
