#coding:utf-8
from django.contrib import admin

from models import Comment


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
	list_display = ("block", "article", "comment", "owner", "status", "create_time", "update_time")
	search_fields = ("content",)
	list_filter = ("block", )

admin.site.register(Comment, CommentAdmin)