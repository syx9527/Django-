"""mysite1 URL Configuration

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
from .views import *

urlpatterns = [
    path('admin', admin.site.urls),
    path("", index),
    #  http://127.0.0.1:8000/page/2003/,
    path('page/2003', page_2003),

    path('page/1', page1_view),
    path('page/2', page2_view),
    path('page/3', page3_view),

    re_path(r'^(?P<a>\d{1,2})/(?P<op>\w+)/(?P<b>\d{1,2})$', call_view),

    path('page/<int:page>', page_view),

    path("test_request", test_request),
    path("test_get_post", test_get_post),
    path("test_html", test_html),
    path("test_if_for", test_if_for),
    path("mycal", test_mycal),

    path("base_index", base_view, name="base_index"),
    path("music_index", music_view),
    path("sport_index", sport_view),

    path('test/url', test_url),

    # path("test_url_result/<int:age>", test_url_result, name='tr'),
    path("test_url_result/<int:age>", test_url_result, name='tr'),

]
