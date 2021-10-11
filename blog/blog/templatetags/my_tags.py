# -*- coding: utf-8 -*-
# @Time : 2021/9/17 15:44
# @Author : 41999
# @Email : 419997284@qq.com
# @File : my_tags.py
# @Project : row.js

from django import template
from blog import models
from django.db.models import Count

register=template.Library()

@register.simple_tag
def multi_tag(x, y):
    return x * y

@register.inclusion_tag("blog/classification.html")
def get_classification_style(username):

    user = models.UserInfo.objects.filter(username=str(username)).first()
    blog = user.blog
    userid = user.nid
    nid = blog.nid  # 用作原地跳转标签匹配
    cate_list = models.Category.objects.filter(blog__nid=nid).values_list("title").annotate(c=Count("Article_category"))
    tag_list = models.Tag.objects.values('pk').annotate(c=Count("article")).values_list("title", "c").filter(
        blog_id=nid)
    year_month = models.Article.objects.filter(user=nid).extra(
        select={"y_m_date": "date_format(create_time,'%%Y-%%m')"}).values(
        'y_m_date').annotate(c=Count("nid")).values_list('y_m_date', 'c')

    return {"username":username, "blog": blog, "cate_list": cate_list, "tag_list": tag_list,"year_month": year_month}