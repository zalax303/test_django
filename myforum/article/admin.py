from django.contrib import admin

from models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("title", "block", "owner", "create_time", "update_time")
	search_fields = ["title", "content", "owner"]
	list_filter = ("block", )

admin.site.register(Article, ArticleAdmin)
