from django.db.models import Count
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.contrib import auth

from .MyForms import UserForm
from .models import *


# Create your views here.


def index(request):
    article_list = Article.objects.all()

    return render(request, "blog/index.html", {"article_list": article_list})


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

    return render(request, 'blog/login.html')


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
                user_obj = UserInfo.objects.create_user(username=user, password=pwd, email=email, avatar=avatar_obj)
            else:
                user_obj = UserInfo.objects.create_user(username=user, password=pwd, email=email)

        else:
            # print(form.cleaned_data)
            # print(form.errors)
            response['msg'] = form.errors
        return JsonResponse(response)

    form = UserForm()
    return render(request, "blog/register.html", {"form": form})


def home_site(request, username):
    """
    个人站点视图函数
    """
    print("username:", username)
    user = UserInfo.objects.filter(blog__site_name=username).first()

    # 判断用户是否存在
    if not user:
        return render(request, "blog/not_found.html")

    # 查询当前站点对象
    blog = user.blog
    userid = user.nid
    nid = blog.nid  # 用作原地跳转标签匹配
    print(nid)

    # 当前用户或者站点对应的所有文章
    # 基于对象查询
    # article_list = user.article_set.all()  # 不知道为啥会报错
    # 基于双下划线查询（跨表查询）
    article_list = Article.objects.filter(user=user)

    # 查询每一个分类名称以及对应的文章数
    ret = Category.objects.values("pk").annotate(c=Count("blog__title")).values("title", "c")
    # cate_list = Category.objects.filter(blog__nid=nid).values_list("title").annotate(c=Count("Article_category"))
    print(ret)

    # 查询当前站点的每一个分类名称以及对应的文章数目; 能用Article_category是因为article包含了外键category
    cate_list = Category.objects.filter(
        blog__nid=nid).values("title").annotate(c=Count("Article_category"))
    print(cate_list)
    # 查询当前站点的每一个标签名称以及对应的文章数
    tag_list = Tag.objects.values('pk').annotate(c=Count("article")).values("title", "c").filter(
        blog_id=nid)
    print(tag_list)
    # 查询当前站点每一个年月的名称以及对应的文章数---单表分组查询 引入函数专门处理日期分组：
    # 方式一
    year_month = Article.objects.filter(user=userid).extra(
        select={"y_m_date": "date_format(create_time,'%%Y-%%m')"}).values('y_m_date').annotate(
        c=Count("nid")).values('y_m_date', 'c')

    # 方式二
    from django.db.models.functions import TruncMonth
    year_month2 = Article.objects.filter(user=userid).annotate(month=TruncMonth("create_time")).values(
        "month").annotate(
        c=Count(nid)).values("month", 'c')
    print(year_month2)

    # return render(request, "blog/home_site.html", {"username": user.username})
    return render(request, "blog/home_site.html", {"username": username, "blog": blog, "article_list": article_list})
