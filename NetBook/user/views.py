import hashlib
import time

from django.shortcuts import *
from .models import User


# Create your views here.

def user_logup(request):
    """
    注册
    GET 返回页面
    POST 处理提交数据
        1.两个密码要保持一致
        2.检查用户名是否可用
        3.满足1，2插入数据 [暂时明文处理]
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'user/logup.html')

    elif request.method == "POST":

        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        old_user = User.objects.filter(username=username)
        message = None
        data = {
            'username': username,
            'password_1': password_1,
            'password_2': password_2,
        }

        """
        哈希算法 - 给定明文，计算出一段定长的，不可逆的值
        md5 - 32位16进制
        场景    1.密码处理  2.文件校验
        """

        md5 = hashlib.md5()
        md5.update(password_1.encode())
        password_m = md5.hexdigest()

        if not (username and password_1 and password_2):
            message = '账号密码不能为空'
        elif old_user:
            message = '用户名已经注册，请重新输入！'
        elif password_1 != password_2:
            message = '两次密码输入不一致，请重新输入！'
            data['password_2'] = None

        if not message:
            try:
                user = User.objects.create(username=username, password=password_m)
                # 免登录一天
                request.session['username'] = username
                request.session['uid'] = user.id

                return redirect('/')

            except Exception as e:
                print("--create user error %s" % e)
                message = '用户名已经注册，请重新输入！'
        return render(request, 'user/logup.html', {
            'message': message,
            'data': data
        })


def user_login(request):

    if request.method == "GET":
        c_username = request.COOKIES.get("username")
        c_uid = request.COOKIES.get('uid')
        if request.session.get('username') and request.session.get('uid'):
            return redirect('/')
        elif c_uid and c_username:
            request.session['username'] = c_username
            request.session['c_uid'] = c_uid
            return redirect('/')
        else:
            return render(request, 'user/login.html')

    if request.method == "POST":

        # 处理数据
        remember = request.POST.get('remember')

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        md5 = hashlib.md5()
        md5.update(password.encode())

        message = None
        if not (username and password):
            message = '账号密码不能为空'
        elif (not user) or (md5.hexdigest() != user[0].password):
            message = '用户名或密码错误！'
        if message:
            return HttpResponse(message)
        else:

            request.session['username'] = username
            request.session['uid'] = user[0].id

            response = redirect('/')
            if remember:
                response.set_cookie('username', username, 3600)
                response.set_cookie('uid', user[0].id, 3600)

            return response


def logout(request):
    # 删除session
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']

    response = HttpResponseRedirect("/")

    if 'username' in request.COOKIES:
        response.delete_cookie('username')
    if 'uid' in request.COOKIES:
        response.delete_cookie('uid')

    return response
