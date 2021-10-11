import os.path
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count, F, Q
from django.db.models.functions import TruncMonth
import PIL, random, json
from blog.models import UserInfo
from blog.Myforms import UserForm
from blog.utils.validCode import get_valide_code_img
from blog import models
from bs4 import BeautifulSoup
from whereabouts import settings


def login(request):
    """
    功能设计：验证码和用户信息的校验
    不区分验证码大小写，统一转换为大写 uppercase
    auth.login:在请求中保留用户id和后端。这样，用户就不必在每次请求时都重新验证。请注意，匿名会话期间的数据集在用户登录时保留。
    auth.authenticate: 从client请求中提取数据，将数据与数据库进行匹配
    response: 字典，作为message传递提示信息
    request.POST: 包含所有前端传递的信息
    auth.login:保存单个用户的单次登录信息
    JsonResponse：Json化后端生成的提示信息

    """
    if request.method == "POST":
        response = {"user": None, "msg": None}
        user = request.POST.get("user")
        # print(user)
        pwd = request.POST.get("pwd")
        # 前端提交的验证码
        valid_code_one = request.POST.get("valid_code")
        valid_code = str(valid_code_one)

        # 后端生成的验证码，由get_validCode_img负责生成
        valid_code_str = request.session.get("valid_code_str")
        # print(valid_code)  # 测试后端在提交前端显示之前保存的验证码
        # print(valid_code_str)  # 测试前端POST请求提交时给出的验证码
        if valid_code.upper() == valid_code_str.upper():
            user = auth.authenticate(username=user, password=pwd)  # 将前端提交的密码与后端MySQL存储的用户名与密码匹配
            if user:
                auth.login(request, user)  # 匹配成功后则将其注册request.user==当前登录对象,存储当前登录对象
                response["user"] = user.username
            else:
                response["msg"] = "username or password error!"
        else:
            response["msg"] = "vali de code error!"
        return JsonResponse(response)

    return render(request, "blog/login.html")


def get_validCode_img(request):
    """
    调用blog/utils/valid_code程序生成代码
    用request.session传递后端生成验证码
    """
    data = get_valide_code_img(request)
    # print(type(data))

    return HttpResponse(data)


def index(request):
    """
    需要导入整个models模块，然后导出所有的文章
    文章数据从models提取出来，然后由views视图将数据渲染的时候传递给首页index,首页index再进行相关的渲染
    """
    article_list = models.Article.objects.all()
    return render(request, "blog/index.html", {"article_list": article_list})


def registry(request):
    """
    UserForm验证提交的用户名，密码，邮箱等数据
    用settings中的media处理头像文件
    如果提交的数据错误，则由一个字典在原页面上显示提示信息
    """
    if request.is_ajax():
        # print(request.POST)  # 输出结果 <QueryDict: {'csrfmiddlewaretoken': [
        # '1DRQx9q2UOwhlL3gRDMwhiGsxOvEmjrt6RgrnJVW4O1zhA6E2IjPAiAofmcfoXxl'], 'avatar': ['undefined']}>
        form = UserForm(request.POST)  # 由UserForm做验证
        # print(form)
        response = {"user": None, "msg": None}  # 用于前端交互，传递message
        if form.is_valid():
            response["user"] = form.cleaned_data.get("user")  # 验证通过则会传递用户名
            # 生成一张用户记录 UserInfo不仅是自己设计的用户表，也是用户验证组件的那一张表
            # 该属性用于处理形成摘要的用户注册信息，不能用UserInfo.objects.create
            user = form.cleaned_data.get("user")
            pwd = form.cleaned_data.get("pwd")
            email = form.cleaned_data.get("email")
            avata_obj = request.FILES.get("avatar")  # 指定前端提交时的字段名字，隶属于formdata对象
            extra = {}

            if avata_obj:
                extra["avatar"] = avata_obj
                UserInfo.objects.create_user(username=user, password=pwd, email=email,
                                             **extra)  # avatar是UserInfo的field， avatar_obj是前端传递的文件
        else:
            # print(form.cleaned_data)
            # print(form.errors)
            response["msg"] = form.errors
        return JsonResponse(response)

    # 实例化对象，
    form = UserForm()
    # form为提示信息
    return render(request, "blog/registry.html", {"form": form})


def logout(request):
    # from django.contrib import auth
    auth.logout(request)  # 等同于request.session.flush
    # return redirect("templates/blog/login.html")
    return redirect("/login/")


def home_site(request, username, **kwargs):
    """
    个人站点视图函数
    """
    user = models.UserInfo.objects.filter(username=str(username)).first()
    # print(user.username)
    if not user:
        return render(request, "blog/not_found.html")
    # 查询当前站点对象以及id
    blog = user.blog
    userid = user.nid
    nid = blog.nid  # 用作原地跳转标签匹配
    # 当前用户或者当前站点对应的所有文章
    article_list = models.Article.objects.filter(user=userid)
    if kwargs:
        condition = kwargs.get("condition")
        param = kwargs.get("param")  # 2012-12

        if condition == "category":

            article_list = article_list.filter(category__title__icontains=param)
        elif condition == 'tag':  # 通过tags字段回到Tag
            article_list = article_list.filter(tags__title__icontains=param)
        else:
            year, month = param.split("-")
            article_list = article_list.filter(create_time__year=year,
                                               create_time__month=month)

    # 查询当前站点的每一个分类名称以及对应的文章数目; 能用Article_category是因为article包含了外键category
    # cate_list = models.Category.objects.filter(blog__nid=nid).values_list("title").annotate(c=Count("Article_category"))
    # 查询当前站点的每一个标签名称以及对应的文章数
    # tag_list = models.Tag.objects.values('pk').annotate(c=Count("article")).values_list("title", "c").filter(
    #     blog_id=nid)
    # 查询当前站点每一个年月的名称以及对应的文章数---单表分组查询
    # 引入函数专门处理日期分组：from django.db.models.functions import TruncMonth
    # year_month = models.Article.objects.filter(user=nid).extra(
    #     select={"y_m_date": "date_format(create_time,'%%Y-%%m')"}).values(
    #     'y_m_date').annotate(c=Count("nid")).values_list('y_m_date', 'c')
    return render(request, "blog/home_site.html", {"username": username, "blog": blog, "article_list": article_list})


def get_classification_data(username):
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

    return {"username": username, "blog": blog, "cate_list": cate_list, "tag_list": tag_list, "year_month": year_month}


def article_detail(request, username, article_id):
    user = models.UserInfo.objects.filter(username=str(username)).first()
    blog = user.blog
    article_obj = models.Article.objects.filter(pk=article_id).first()
    comment_list = models.Comment.objects.filter(article_id=article_id)
    return render(request, "blog/article_detail.html", locals())


def updown(request):
    """
    用于处理点赞行为执行后前端通过POST请求发送过来的数据
    json用于反序列化
    from django.db.models import  F 用于自加一
    from django.http import JsonResponse 用于返回字典
    """
    # print(request.POST)
    article_id = request.POST.get("article_id")
    is_up = json.loads(request.POST.get("is_up"))  # 'true'
    # print(is_up)
    # print(type(is_up))
    user_id = request.POST.get("user_id")  # 由session提供
    # print(user_id)

    obj = models.ArticleUpDown.objects.filter(user_id=user_id, article_id=article_id).first()
    response = {"state": True}
    if not obj:
        articleupdown = models.ArticleUpDown.objects.create(user_id=user_id, article_id=article_id, is_up=is_up)
        queryset = models.Article.objects.filter(pk=article_id)
        if is_up:
            queryset.update(up_count=F("up_count") + 1)
        else:
            queryset.update(down_count=F("down_count") + 1)
    else:
        response["state"] = False
        response["handled"] = obj.is_up

    return JsonResponse(response)


def comment(request):
    """
    from django.db import transaction  : 用于数据库事务同步
    """

    # print(request.POST)
    article_id = request.POST.get("article_id")
    pid = request.POST.get("pid")
    content = request.POST.get("content")
    user_id = request.POST.get("user_id")
    article_title = models.Article.objects.get(nid=article_id)

    with transaction.atomic():
        comment_obj = models.Comment.objects.create(user_id=user_id, article_id=article_id, content=content,
                                                    parent_comment_id=pid)
        models.Article.objects.filter(pk=article_id).update(comment_count=F("comment_count") + 1)

    response = {}

    response["create_time"] = comment_obj.create_time.strftime("%Y-%m-%d %X")
    response["username"] = comment_obj.user.username
    response["content"] = content

    # 发送邮件
    from django.core.mail import send_mail
    from whereabouts import settings
    import threading
    #
    # send_mail(
    #     "您的文章%s新增了一条评论内容"%article_title,
    #     content,
    #     settings.EMAIL_HOST_USER,
    #     ["419997284@qq.com"]
    # )

    t = threading.Thread(target=send_mail, args=(
        "您的文章%s新增了一条评论内容" % article_title,
        content,
        settings.EMAIL_HOST_USER,
        ["419997284@qq.com"]
    ))

    t.start()

    return JsonResponse(response)


def get_comment_tree(request):
    article_id = request.GET.get("article_id")
    ret = list(models.Comment.objects.filter(article_id=article_id).order_by("pk").values("pk", "content",
                                                                                          "parent_comment_id"))

    return JsonResponse(ret, safe=False)


@login_required
def cn_backend(request):
    article_list = models.Article.objects.filter(user=request.user)

    return render(request, "backend/backend.html", locals())


@login_required
def add_article(request):
    """
    from bs4 import BeautifulSoup 负责解析网页标签
    """
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        soup = BeautifulSoup(content, "html.parser")
        # 过滤标签
        for tag in soup.find_all():
            print(tag.name)
            if tag.name == "script":
                tag.decompose()

        desc = soup.text[0:150]

        models.Article.objects.create(title=title, desc=desc, content=str(soup), user=request.user)
        return redirect("/blog/cn_backend/")

    return render(request, "backend/add_article.html")


def upload(request):
    """
    编辑器上传文件接受视图函数
    url : 为拼接结果，在服务器上固定位置加上图片的名称，注意media前有斜杠
    return : 返回值为json序列化结果，将url传递给前端的编辑器
    """

    # print(request.FILES)
    img = request.FILES.get("upload_img")
    print(img.name)

    path = os.path.join(settings.MEDIA_ROOT, "add_article_img", img.name)
    with open(path, "wb") as f:
        for line in img:
            f.write(line)

    response = {
        "error": 0,
        "url": "/media/add_article_img/%s" % img.name
    }

    return HttpResponse(json.dumps(response))
