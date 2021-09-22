from django.core.paginator import Paginator
from django.shortcuts import *
from .models import *


# Create your views here.


# @check_login

def add_view(request):
    if request.method == "GET":
        print('888')
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


def test_mw(request):
    print('---test_mw view in ---')
    return HttpResponse('middleware test')


def test_page(request):
    # /note/test_page/4
    # /note/test_page/?page=1
    page_num = request.GET.get('page', 1)
    all_data = ['a', 'b', 'c', 'd', 'e']
    # 初始化paginator对象
    paginator = Paginator(all_data, 2)

    # 初始化 具体页码的page对象
    c_page = paginator.page(int(page_num))

    return render(request, 'note/test_page.html', {'c_page': c_page})
