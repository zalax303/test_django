# coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from models import Block


# Create your views here.
def block_list(request):
	blocks = Block.objects.all().order_by("-id")  # 负号代表倒序排序
	return render_to_response("block_list.html", {"blocks": blocks})  # {}字典里面代表熏染变量
