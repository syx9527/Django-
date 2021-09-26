from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User

# 创建用户
# u = User.objects.create_user(username='ly', password='123')

# 创建超级用户
# su = User.objects.create_superuser(username='syx', password='123')

# 基本模型操作 - 校验密码
from django.contrib.auth import authenticate

# 校验成功返回对像，否则返回None
user = authenticate(username='syx', password='1235')
print(user)

# 修改密码

# from django.contrib.auth.models import User

try:
    user = User.objects.get(username='xiaoLiu')
    user.set_password('654321')
    user.save()
    print('修改密码成功!')
except:
    print('修改密码失败！')

# 登录状态保持
from django.contrib.auth import login


def login_view(request):
    user = authenticate(username='ly', password='123')

    login(request, user)


# 登录状态校验

from django.contrib.auth.decorators import login_required


@login_required
def index_view(request):
    # 该视图必须为用户登录状态下才可访问
    # 当前登录用户可通过request.user获取
    login_user = request.user
    # ……


# 登录状态取消

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
