from django.shortcuts import *
from .models import *


# Create your views here.

def check_login(fn):
    def wrap(request, *args, **kwargs):
        if 'username' not in request.session or 'uid' not in request.session:
            c_username = request.COOKIES.get("username")
            c_uid = request.COOKIES.get("uid")
            if not c_uid or not c_uid:
                return HttpResponseRedirect('/user/login')
            else:
                request.session['username'] = c_username
                request.session['uid'] = c_uid

        return fn(request, *args, **kwargs)

    return wrap


@check_login
def add_view(request):
    if request.method == "GET":
        return render(request, 'note/add_note.html')

    if request.method == "POST":

        # 处理数据
        uid = request.session.get('uid')
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title or content:
            Note.objects.create(title=title, content=content, user_id=uid)
            return HttpResponse("添加笔记成功")
        else:
            return HttpResponseRedirect(request.path)
