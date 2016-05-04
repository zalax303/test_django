#coding:utf-8
from django.db import models
from django.contrib.auth.models import User


class ActivateCode(models.Model):
	owner = models.ForeignKey(User, verbose_name="用户")
	code = models.CharField(verbose_name="激活码", max_length=100)

	expire_timestamp = models.DateTimeField()
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
