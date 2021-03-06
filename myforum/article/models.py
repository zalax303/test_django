# coding:utf-8
from django.contrib.auth.models import User
from django.db import models

from block.models import Block


# Create your models here.
class Article(models.Model):
	block = models.ForeignKey(Block, verbose_name=u"所属板块")
	owner = models.ForeignKey(User, verbose_name=u"作者")
	title = models.CharField(verbose_name=u"标题", max_length=100)
	content = models.CharField(verbose_name=u"内容", max_length=10000)
	status = models.IntegerField(verbose_name=u"状态", choices=((0, u"普通"), (-1, u"剔除"), (10, u"精华")), default=0)
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u"文章"
		verbose_name_plural = u"文章"
