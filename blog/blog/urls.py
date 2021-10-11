# -*- coding: utf-8 -*-
# @Time : 2021/9/19 21:37
# @Author : 41999
# @Email : 419997284@qq.com
# @File : urls.py
# @Project : row.js
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url

urlpatterns = [
    # 点赞或者踩之后的页面跳转
    url(r'^updown/$', views.updown, name='updown'),
    # 用于提交评论
    path('comment/', views.comment, name='comment'),
    # 负责图片上传功能
    path('upload/', views.upload, name='upload'),
    # 用于展示评论树
    path('get_comment_tree/', views.get_comment_tree, name='get_comment_tree/'),
    # 后台管理页面 测试时只能在前面文章页的基础上手动添加URL段，不能直接从URL访问
    # http://127.0.0.1:8001/blog/cn_backend/
    re_path("cn_backend/$", views.cn_backend),
    # http://127.0.0.1:8001/blog/cn_backend/add_article/
    re_path("cn_backend/add_article/$", views.add_article),

]