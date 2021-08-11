from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

POST_FORM = """
<form method='post' action='/test_get_post'>
    用户名:<input type='text' name = "username">
    密码:<input type='text' name = "password">
<input type="submit" value="登录">
</form>
"""


def sai_hai():
    return "HIHIHI"


class Dog:

    def say(self):
        return "Wangwangwang"

    def eat(self, ):
        return "狗吃骨头"


def index(request):
    html = '<h1>这是我的首页</h1>'
    return HttpResponse(html)


def page1_view(request):
    html = '这是编号为1的网页'
    return HttpResponse(html)


def page2_view(request):
    html = '这是编号为2的网页'
    return HttpResponse(html)


def page3_view(request):
    html = '这是编号为3的网页'
    return HttpResponse(html)


def page_view(request, page):
    html = '这是编号为%s的网页!!' % page
    return HttpResponse(html)


def call_view(request, a, op, b):
    a = int(a)
    b = int(b)

    if op == "add":
        op = '+'
        c = a + b
    elif op == "c":
        op = "*"
        c = a * b
    html = ("%s %s %s " + "= %s") % (a, op, b, c)
    return HttpResponse(html)


def page_2003(request):
    html = '<h1>这是第一个页面</h1>'
    return HttpResponse(html)


def test_request(request):
    print("path info is ", request.path_info)

    print("method is ", request.method)

    print("querystring is ", request.GET)

    # return HttpResponse("test request ok")

    return HttpResponseRedirect('page/1')


def test_get_post(request):
    if request.method == "GET":
        print("a:", request.GET)
        print("a:", request.GET.get('a', '100'))
        print("c:", request.GET.get('c', '-1'))

        # 问卷调查 -from get 兴趣爱好  - 复选框
        print("list:", request.GET.getlist('a'))

        return HttpResponse(POST_FORM)
    elif request.method == "POST":
        print('username is:', request.POST['username'])
        print('password is:', request.POST['password'])
        return HttpResponse('post is ok')
    else:
        pass

    return HttpResponse("--test get and post is ok--")


def test_html(request):
    # 方案一
    # t = loader.get_template('test_html.html')
    # hrml = t.render()
    # return HttpResponse(hrml)

    # 方案二
    dic = {}
    dic['int'] = 88
    dic['str'] = 'shaoyuexin'
    dic['list'] = ['jup', 'lod', 'ul']
    dic['dict'] = {'a': 9, 'b': '乌拉'}
    dic['function'] = sai_hai
    dic['class_obj'] = Dog()
    dic['script'] = "<script>alert(111111)</script>"

    return render(request, 'test_html_param.html', dic)


def test_if_for(request):
    dic = {}
    dic['x'] = 20
    dic['list'] = ['Tom', 'Jack', 'Lily']
    return render(request, 'test_if_for.html', dic)


def test_mycal(request):
    if request.method == "GET":
        return render(request, 'mycal.html')
    elif request.method == "POST":
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']

        if op == 'add':
            result = x + y
        elif op == "sub":
            result = x - y
        elif op == "mul":
            result = x * y
        elif op == 'div':
            result = x / y
        else:
            pass
        # dic = {}
        # dic['x'] = x
        # dic['y'] = y
        # dic['op'] = op
        return render(request, 'mycal.html', locals())


def base_view(request):
    username = 'ZhangSan'
    return render(request, 'base.html', locals())


def music_view(request):
    return render(request, 'music.html')


def sport_view(request):
    return render(request, 'sport.html')


def test_url(request):
    return render(request, 'test_url.html')


def test_url_result(request, age):
    # 302跳转
    from django.urls import reverse
    url = reverse("base_index")
    print(url)
    return HttpResponseRedirect(url)

    # return HttpResponse("---test url res is ok---")
