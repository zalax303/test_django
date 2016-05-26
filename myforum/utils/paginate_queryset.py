# coding:utf-8
from django.core.paginator import Paginator


def paginate_queryset(objs, page_no, cnt_per_page=10, half_show_length=5):
	'''
	:param objs: 需要显示的内容列表
	:param page_no: 想要展示的页码
	:param cnt_per_page: 每页可以显示多少条记录
	:param half_show_length: 当前显示的页码最多(最少)可以看到多少页码
	:return:
	'''
	p = Paginator(objs, cnt_per_page)
	if page_no > p.num_pages:
		page_no = p.num_pages
	if page_no <= 0:
		page_no = 1
	page_links = [i for i in range(page_no - half_show_length, page_no + half_show_length + 1)
				  if i > 0 and i <= p.num_pages]
	page = p.page(page_no)
	previous_link = page_links[0] - 1
	next_link = page_links[-1] + 1
	paginate_data = {
					"has_pervious": previous_link > 0,
					"has_next": next_link <= p.num_pages,
					"previous_link": previous_link,
					"next_link": next_link,
					"page_cnt": p.num_pages,
					"current_no": page_no,
					"page_links": page_links
					}
	return page.object_list, paginate_data
