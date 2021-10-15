from django.db.models import Count
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.contrib import auth
from django.template import Context
from django.template.loader import get_template

from .MyForms import UserForm
from .models import *

from .utils.img import cat_img
from django.conf import settings
from django.db.models.functions import TruncMonth
from django.conf import settings


# Create your views here.


def index(request):
    return render(request, "Tale/base.html", {"user": {"username": settings.ALL_USER}})


def about(request):
    article_list = Article.objects.all()

    # return render(request, "blog/index.html", {"article_list": article_list})
    return render(request, "Tale/about.html", )


def other(request, htmlname):
    # article_list = Article.objects.all()
    template_name = f"Tale/{htmlname}"
    # return render(request, "blog/index.html", {"article_list": article_list})
    return render(request, template_name=template_name, )


# 登录
def login(request):
    if request.method == "POST":
        response = {"user": None, "msg": None, "code": None}
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        valid_code = request.POST.get("valid_code")
        valid_code_str = request.session.get("valid_code_str")

        # 检验验证码
        if valid_code.upper() == valid_code_str.upper():
            user = auth.authenticate(username=user, password=pwd)
            if user:
                auth.login(request, user)  # request.user==当前登录对象
                response['user'] = user.username
                response['code'] = 1
            else:
                response['msg'] = "用户名密码错误!"
                response['code'] = -1
        else:
            response["msg"] = "验证码错误"
            response['code'] = 0
        return JsonResponse(response)

    return render(request, 'login_out/index.html')


# 用户注销

def logout(request):
    auth.logout(request)  # request.session.flush()

    return HttpResponseRedirect("/")


def get_ValidCode_img(request):
    from .utils.validCode import get_valid_code_img

    data = get_valid_code_img(request)

    return HttpResponse(data)


# 注册
def register(request):
    if request.is_ajax():

        form = UserForm(request.POST)

        # print(request.POST)
        response = {"user": None, "msg": None}
        if form.is_valid():
            print(form.cleaned_data)
            response['user'] = form.cleaned_data.get("user")

            # 生成一条用户记录

            user = form.cleaned_data.get("user")
            print("user:", user)
            pwd = form.cleaned_data.get("pwd")
            email = form.cleaned_data.get("email")
            avatar_obj = request.FILES.get("avatar")

            if avatar_obj:
                import os
                print(settings.BASE_DIR)
                path = os.path.join(settings.BASE_DIR, 'media', "avatars", avatar_obj.__str__())

                user_obj = UserInfo.objects.create_user(username=user, password=pwd, email=email, avatar=avatar_obj)
                cat_img(path)

            else:
                user_obj = UserInfo.objects.create_user(username=user, password=pwd, email=email)

        else:
            # print(form.cleaned_data)
            # print(form.errors)
            response['msg'] = form.errors
        return JsonResponse(response)

    form = UserForm()
    return render(request, "blog/register.html", {"form": form})


def home_site(request, stiename):
    """
    个人站点视图函数
    """
    print("username:", stiename)
    user = UserInfo.objects.filter(blog__site_name=stiename).first()

    # 判断用户是否存在
    if not user:
        return render(request, "blog/not_found.html")
    # 查询当前站点对象
    blog = user.blog
    return render(request, "Tale/author.html",
                  {"user": user, "blog": blog, })


# 查询文章列表
def query_article_list(request):
    if request.is_ajax():

        id = request.POST.get("id")
        name = request.POST.get("name")
        username = request.POST.get("username")
        print("username", username)
        if username != settings.ALL_USER:

            if name == 'tag':
                article_list = Article.objects.filter(user__username=username, tags__title=id)
            elif name == "cate":
                article_list = Article.objects.filter(user__username=username, category__title=id)
            elif name == "month":
                year, month = id.split('-')
                article_list = Article.objects.filter(user__username=username).filter(
                    create_time__year=year, create_time__month=month)

            elif name == "all":
                article_list = Article.objects.filter(user__username=username)
            else:
                return JsonResponse({"code": 0})
        else:

            if name == 'tag':
                article_list = Article.objects.filter(tags__title=id)
            elif name == "cate":
                article_list = Article.objects.filter(category__title=id)
            elif name == "month":
                year, month = id.split('-')
                article_list = Article.objects.filter().filter(
                    create_time__year=year, create_time__month=month)
            else:
                article_list = Article.objects.filter()

        t = get_template("Tale/article_list.html")
        content_html = t.render({'article_list': article_list, })

        response = {"content_html": content_html, "code": 1}

        return JsonResponse(response)


# 获取标签列表
def query_tag_list(request):
    if request.is_ajax():
        id = request.POST.get("id")
        name = request.POST.get("name")
        username = request.POST.get("username")

        if username != settings.ALL_USER:
            user = UserInfo.objects.filter(username=username).first()

            # 查询当前站点对象
            blog = user.blog
            userid = user.nid
            nid = blog.nid  # 用作原地跳转标签匹配
            # 查询当前站点的每一个标签名称以及对应的文章数
            tag_list = Tag.objects.values('pk').annotate(c=Count("article")).values("title", "c").filter(
                blog_id=nid)
            # print("tag_list:", tag_list)
        else:
            tag_list = Tag.objects.values('pk').annotate(c=Count("title")).values("title", "c")
            print(tag_list)
        t = get_template("Tale/tag_list.html")
        content_html = t.render({'tag_list': tag_list, })

        response = {"content_html": content_html, "code": 1}
        return JsonResponse(response)


# 获取分类列表
def query_cate_list(request):
    if request.is_ajax():
        id = request.POST.get("id")
        name = request.POST.get("name")
        username = request.POST.get("username")

        if username != settings.ALL_USER:
            print(username)
            user = UserInfo.objects.filter(username=username).first()

            # 查询当前站点对象
            blog = user.blog
            userid = user.nid
            nid = blog.nid  # 用作原地跳转标签匹配
            # 查询当前站点的每一个标签名称以及对应的文章数
            cate_list = Category.objects.filter(
                blog__nid=nid).values("title").annotate(c=Count("Article_category"))
        else:
            cate_list = Category.objects.filter().values("title").annotate(c=Count("Article_category"))
        print("cate_list:", cate_list)

        t = get_template("Tale/cate_list.html")
        content_html = t.render({'cate_list': cate_list, })

        response = {"content_html": content_html, "code": 1}
        return JsonResponse(response)


# 获取归档列表
def query_month_list(request):
    if request.is_ajax():
        username = request.POST.get("username")
        print(username)
        if username != settings.ALL_USER:
            user = UserInfo.objects.filter(username=username).first()
            print(username)
            # 查询当前站点对象
            blog = user.blog
            userid = user.nid
            nid = blog.nid  # 用作原地跳转标签匹配
            # 查询当前站点的每一个标签名称以及对应的文章数
            year_month = Article.objects.filter(user=userid).annotate(month=TruncMonth("create_time")).values(
                "month").annotate(
                c=Count(nid)).values("month", 'c')
        else:
            year_month = Article.objects.filter().annotate(month=TruncMonth("create_time")).values(
                "month").annotate(
                c=Count('nid')).values("month", 'c')



        t = get_template("Tale/year_month.html")
        content_html = t.render({'year_month': year_month, })

        response = {"content_html": content_html, "code": 1}
        return JsonResponse(response)
