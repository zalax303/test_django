#coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext  #导入模板
from block.models import Block
from models import Article
from django.contrib.auth.models import User

#
# Create your views here.


def article_list(request, block_id):  #block_id来自于url中的block_id变量
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)  #get方法要求只返回一个结果
	articles = Article.objects.filter(block=block).order_by("-update_time")
	#filter相当于sql where条件 -代表倒序
	return render_to_response("article_list.html", {"articles": articles, "block": block},
							context_instance=RequestContext(request))  #必加该参数

def create_article(request, block_id):
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)  #get方法要求只返回一个结果
	if request.method == "GET":
		return render_to_response("article_create.html", {"b": block},
								context_instance=RequestContext(request))
	else:  #POST
		title = request.POST["title"].strip()
		content = request.POST["content"].strip()
		if not title or not content:
			pass
			# messages.add_message("article_create.html",{"b": block, "title":title, "content": content},
			# 					 context_instance=RequestContext(request))
		# owner = User.objects.all()[0]
		# news_article = Article(block=block, owner=owner, content=content, title=title)
		# news_article.save()
		# messages.add_message(request, message.INFO, u'文章发布成功')
		# return redirect(reverse("article_list", args=[block.id]))