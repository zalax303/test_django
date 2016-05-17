# coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from models import Block


# Create your views here.
def block_list(request):
	blocks = Block.objects.all().order_by("-id")  # Object代表是Block这张表,负号代表倒序排序
	return render_to_response("block_list.html", {"blocks": blocks}, context_instance=RequestContext(request))  # {}字典里面代表熏染变量
	# return render(request, "block_list.html", {"blocks": blocks}) 也可以使用这种方式,自动导入RequestContext

# def index(request): #静态页面
# 	return render(request, "index.html")
