"""whereabouts URL Configuration

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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url


urlpatterns = [
    path('blog/', include('blog.urls')),
    # 负责图片上传功能
    path('upload/', views.upload, name='upload'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    # http://127.0.0.1:8001/login/
    path('login/', views.login),
    # http://127.0.0.1:8001/logout/
    path('logout/', views.logout),
    path('get_validCode_img/', views.get_validCode_img),
    # http://127.0.0.1:8001/index/
    path('index/', views.index),
    # 用于提交评论
    # path('comment/', views.comment, name='comment'),
    # http://127.0.0.1:8001/
    re_path('^$', views.index),
    # http://127.0.0.1:8001/registry/
    path('registry/', views.registry),
    # 个人站点的原地跳转[点击标签触发内容]
    re_path('^(?P<username>\w+)/(?P<condition>tag|category|archive)/(?P<param>.*)/$', views.home_site),
    # 个人站点URL
    re_path('^(?P<username>\w+)/$', views.home_site),
    # 文章页
    re_path('^(?P<username>\w+)/article/(?P<article_id>\d+)$', views.article_detail),

]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
