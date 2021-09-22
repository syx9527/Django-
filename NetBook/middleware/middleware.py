from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.utils.deprecation import MiddlewareMixin
import re


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


class Middleware(MiddlewareMixin):

    def process_request(self, request):
        # 获取ip
        ip = request.META['REMOTE_ADDR']
        print(ip)
        path_info = request.path_info
        print(path_info)
        print('middleware process_request do ---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('middleware process_view do ---')

    def process_response(self, request, response):
        print('middleware process_response do ---')
        return response


class Middleware_2(MiddlewareMixin):

    def process_request(self, request):
        print('middleware*2 process_request do ---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('middleware*2 process_view do ---')

    def process_response(self, request, response):
        print('middleware*2 process_response do ---')
        return response


class VisitLimit(MiddlewareMixin):
    visit_times = {}

    def process_request(self, request):
        ip_address = request.META['REMOTE_ADDR']
        path_url = request.path_info
        if not re.match(r'^/note', path_url):
            return
        times = self.visit_times.get(ip_address, 0)

        print('ip', ip_address, '已经访问', times)
        self.visit_times[ip_address] = times + 1
        if times < 5:
            return

        return HttpResponse(f'您已经访问过 {times} 次，访问被禁止！')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('middleware*2 process_view do ---')
        path_url = request.path_info
        if re.match(r'(^/user/log)|(^/$)', path_url):
            print('***********')
            return
        elif 'username' not in request.session or 'uid' not in request.session:
            c_username = request.COOKIES.get("username")
            c_uid = request.COOKIES.get("uid")
            print(c_uid, c_username)
            if not c_uid or not c_uid:
                return HttpResponseRedirect('/user/login')
            else:
                request.session['username'] = c_username
                request.session['uid'] = c_uid
            return callback

    def process_response(self, request, response):
        print('middleware*2 process_response do ---')
        return response
