from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index_view(request):
    #

    return HttpResponse("新闻频道主页")