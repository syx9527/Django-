from django.shortcuts import *


def test_static(request):
    # #
    return render(request, "test_static.html")


def test_index(request):
    # return redirect('book/all_book/')
    # return redirect('admin/')
    return redirect('set_cookies/')


def set_cookies(request):
    response = HttpResponse("set cookies is ok")
    response.set_cookie("uname", 'gxn', 500)
    response.set_cookie("s", 'gxn', 500)
    return response


def get_cookies(request):
    value = request.COOKIES.get('uuname')

    return HttpResponse('values is %s' % value)


def set_session(request):
    request.session['uname'] = "dsb"

    return HttpResponse("set session is OK")


def get_session(request):
    value = request.session.get('uname', None)

    return HttpResponse("session value is %s" % value)
