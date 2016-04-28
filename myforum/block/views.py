# coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from models import Block


# Create your views here.
def block_list(request):
	blocks = Block.objects.all().order_by("-id")  # Object代表是Block这张表,负号代表倒序排序
	return render_to_response("block_list.html", {"blocks": blocks})  # {}字典里面代表熏染变量

# def index(request): #静态页面
# 	return render(request, "index.html")
