# coding:utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Block(models.Model):
    name = models.CharField(verbose_name=u"名字", max_length=1000)
    desc = models.CharField(verbose_name=u"描述", max_length=1000)
    manger = models.ForeignKey(User, verbose_name=u"管理员")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"板块"
        verbose_name_plural = u"板块"