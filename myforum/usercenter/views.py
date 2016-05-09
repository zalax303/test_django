#coding:utf-8
import datetime
import uuid

from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext

from models import ActivateCode


def register(request):
	error = ""
	if request.method == 'GET':
		return render_to_response("usercenter_register.html", {}, context_instance=RequestContext(request))
	else:
		username = request.POST["username"].strip()
		email = request.POST["email"].strip()
		password = request.POST["password"].strip()
		re_password = request.POST["re_password"].strip()
		if not username or not email or not password:
			error = u"不允许为空"
		if password != re_password:
			error = u"密码不一致"
		if User.objects.filter(username=username).count() > 1:
			error = u"用户已经存在"
		if not error:
			user = User.objects.create_user(username=username, password=password, email=email)
			user.is_active = 0
			user.save()

			new_code = str(uuid.uuid4().replace("-", ""))   #生成随机码
			expire_time = datetime.datetime.now() + datetime.timedelta(days=2)  #需要两天之内激活
			code_record = ActivateCode(owner=user, code=new_code, expire_timestamp=expire_time)
			code_record.save()

			activate_link = "http://%s%s" % (request.get_host(), reverse("usercenter_activate", args=[new_code]))
			send_mail(u"发送激活邮件", u"你的激活链接为%s" % (activate_link,), '281966779@qq.com', [email] ,
					  fail_silently=False)  #发送失败需要报错
		else:
			return render_to_response("usercenter_register.html", {"error":error},
									context_instance=RequestContext(request))
		return redirect(reverse("login"))


def activate(request, code):
	query = ActivateCode.objects.filter(code=code, expire_timestamp__gte=datetime.datetime.now())
	# expire_timestamp__gte表示这个时间大于现在
	if query.count() > 0:
		code_record = query[0]
		code_record.owner.is_active = 1
		code_record.owner.save()
		return HttpResponse(u"激活成功")
	else:
		return HttpResponse(u"激活失败")