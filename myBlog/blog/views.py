import requests
from django.shortcuts import render
import random
from django.http import HttpResponse, JsonResponse
from django.contrib import auth
from .MyForms import UserForm


# Create your views here.
def index(request):
    return render(request, "blog/index.html")


def login(request):
    if request.method == "POST":
        response = {"user": None, "msg": None, "code": None}
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        valid_code = request.POST.get("valid_code")
        valid_code_str = request.session.get("valid_code_str")

        # 检验验证码
        if valid_code == valid_code_str:
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


def get_ValidCode_img(request):
    from .utils.validCode import get_valid_code_img

    data = get_valid_code_img(request)

    return HttpResponse(data)


def register(request):
    if request.is_ajax():
        print(request.POST)
        form = UserForm(request.POST)

        response = {"user": None, "msg": None}
        if form.is_valid():
            response['user'] = form.cleaned_data.get("user")
        else:
            print(form.cleaned_data)
            print(form.errors)
            response['msg'] = form.errors
        return JsonResponse(response)

    form = UserForm()
    return render(request, "blog/register.html", {"form": form})
