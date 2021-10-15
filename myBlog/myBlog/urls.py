"""myBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from blog.views import *
from django.conf import settings
from django.views import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
    path('index/', index),
    path('query_article_list/', query_article_list, name="article"),
    path('query_tag_list/', query_tag_list, name="tag"),
    path('query_cate_list/', query_cate_list, name="cate"),
    path('query_month_list/', query_month_list, name="month"),

    path('about/', about),
    re_path('^$', index),
    path("get_validCode_img/", get_ValidCode_img),

    # media配置
    re_path(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    re_path('^(?P<htmlname>.*?\.html)$', other),
    # 用户站点
    re_path('^(?P<stiename>\w+)/$', home_site),

    re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}),

]
