from upload_app.models import Content
from django.core.paginator import Paginator
from django.shortcuts import *
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


def upload(request):
    if request.method == "GET":
        a
        return render(request, 'uploadFile.html')

    elif request.method == "POST":
        """
        用request.FILES取文件框的内容
        file = request.FILES['XXX']
            说明: 
            1，FILES的key 对应页面中file框的name值
            2， file 绑定文件流对象,
            3, file.name文件名
            4, file.file文件的字节流数据
        """
        # 1.传统方案，传统open
        # userFile = request.FILES['userFile']
        # print('上传的文件是:' + userFile.name)
        # filename = settings.MEDIA_ROOT / userFile.name
        #
        # with open(filename, 'wb') as f:
        #     data = userFile.file.read()
        #     f.write(data)

        # 2.借助ORM；
        # 字段FileField(upload='子目录名')

        title = request.POST.get('title')
        myfile = request.FILES['myfile']

        Content.objects.create(desc=title, myfile=myfile)
        return HttpResponse("上传成功" + myfile.name + '成功')
