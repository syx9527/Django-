# -*- coding: utf-8 -*-
# @Time : 2021/8/27 10:10
# @Author : 41999
# @Email : 419997284@qq.com
# @File : Myforms.py
# @Project : whereabouts
from django import forms
from django.forms import widgets
from blog.models import UserInfo
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError


class UserForm(forms.Form):
    """均为登录时需要校验的字段"""
    user = forms.CharField(max_length=32, error_messages={"required": "该字段必填，请仔细检查"}, label="用户名",
                           widget=widgets.TextInput(attrs={"class": "form-control"}))
    pwd = forms.CharField(max_length=32, label="密码", widget=widgets.PasswordInput(attrs={"class": "form-control"}))
    re_pwd = forms.CharField(max_length=32, label="确认密码", widget=widgets.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(max_length=32, label="邮箱", widget=widgets.EmailInput(attrs={"class": "form-control"}))

    def clean_user(self):
        """局部钩子：校验用户创建时输入的用户名和MySQL存储的用户名"""
        val = self.cleaned_data.get("user")
        user = UserInfo.objects.filter(username=val).first()
        if not user:
            return val
        else:
            raise ValidationError("该用户已注册！")

    def clean(self):
        """全局钩子：校验两次输入的密码是否一致"""
        # self是实例化对象，form = UserForm(request.POST)
        pwd = self.cleaned_data.get("pwd")
        re_pwd = self.cleaned_data.get("re_pwd")
        if pwd and re_pwd:
            if pwd == re_pwd:
                # print(self.cleaned_data)
                return self.cleaned_data
            else:
                raise ValidationError("两次密码不一致")
        else:
            return self.cleaned_data
