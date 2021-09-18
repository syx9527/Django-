import time

from django.shortcuts import HttpResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache

"""
局部缓存
缓存API的使用
1.cache.set(key,value,timeout) 存储缓存
    key:缓存的key,字符串类型
    value:Python对象
    timeout:缓存存储时间(s),默认为CACHES中的TIMEOUT值
    返回值：None
    
2.cache.get(key) - 获取缓存
    key:缓存的key
    返回值：为key的具体值，如果没有数据，则返回None
    
3.cache.add(key,value) - 存储缓存，只在key不存在时生效
    返回值：True or False

4.cache.get_or_set(key,value,timeout) - 如果未获取到数据，则执行set操作
    返回值：value

5.cache.set_many(dict,timeout) - 批量存储缓存
    dic:key和value的字典
    timeout:存储时间(s)
    返回值:插入不成功的key的数组

6.cache.get_many(key_list) - 批量获取缓存数据
    key_list:包含key的数组
    返回值:取到的key和value的字典
    
7.cache.delete(key) - 删除key的缓存数据
    返回值:None
    
8.cache.delete_many(key_list) - 批量删除
    返回值：None
    
"""


@cache_page(15)
def test_cache(request):
    t = time.time()
    return HttpResponse('time is %s' % int(t))
