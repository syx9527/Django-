# -*- coding: utf-8 -*-
# @Time : 2021/8/10 22:13
# @Author : 41999
# @Email : 419997284@qq.com
# @File : forms.py
# @Project : whereabouts

from django.http import HttpResponse
from django.shortcuts import render


# 表单
def search_form(request):
    return render(request, '')


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
