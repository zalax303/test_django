# coding:utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext  # 导入模板
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from block.models import Block
from models import Article


def article_list(request, block_id):  # block_id来自于url中的block_id变量
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)  # get方法要求只返回一个结果
	articles = Article.objects.filter(block=block).order_by("-update_time")
	# filter相当于sql where条件 -代表倒序
	# 分页
	page_no = int(request.GET.get("page_no", "1"))

	p = Paginator(articles, 1)
	if page_no > p.num_pages:
		page_no = p.num_pages
	if page_no <= 0:
		page_no = 1
	page_links = [i for i in range(page_no - 5, page_no + 6) if i > 0 and i <= p.num_pages]
	page = p.page(page_no)
	previous_link = page_links[0] - 1
	next_link = page_links[-1] + 1

	# return render_to_response("article_list.html", {"articles": articles,
	# 												"blocks": block}, #参数不要使用block跟模板的名字重复了
	# 						context_instance=RequestContext(request))  #必加该参数

	return render_to_response("article_list.html", {"articles": page.object_list,
													"blocks": block,
													"has_pervious": previous_link > 0,
													"has_next": next_link <= p.num_pages,
													"previous_link": previous_link,
													"next_link": next_link,
													"page_cnt": p.num_pages,
													"current_no": page_no,
													"page_links": page_links
													},  # 参数不要使用block跟模板的名字重复了
							  context_instance=RequestContext(request))  # 必加该参数


@login_required  # 强制只有登入的用户才能发文章
def create_article(request, block_id):
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)  # get方法要求只返回一个结果
	if request.method == "GET":
		return render_to_response("article_create.html", {"b": block},
								  context_instance=RequestContext(request))
	else:  # POST
		title = request.POST["title"].strip()
		content = request.POST["content"].strip()
		if not title or not content:
			# pass
			messages.add_message(request, messages.ERROR, u'标题和内容不允许为空')
			return render_to_response("article_create.html",
									  # {"b": block, "title": title, "content": content},#可以不需要这些参数只为传入到html时候用的
									  context_instance=RequestContext(request))  # 停留在当前页面
		else:
			owner = User.objects.all()[0]  # TODO
			news_article = Article(block=block, owner=request.user, content=content, title=title)
			news_article.save()
			messages.add_message(request, messages.INFO, u'文章发布成功')
			return redirect(reverse("article_list",
									args=[block.id]))  # 根据url名称反查url地址(返回一个字符串) 等同于html {% url 'URL名称' 位置参数 关键字参数 %}


def article_detail(request, article_id):
	article_id = int(article_id)
	article = Article.objects.get(id=article_id)
	return render_to_response("article_detail.html", {"article": article},
							  context_instance=RequestContext(request))
