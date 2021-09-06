from django.test import TestCase
from bookstore.models import Author, Book
from django.db.models import *

"""
聚合查询
聚合函数：Sum,Avg,Count,Max,Min
"""

"""
整体聚合

语法：MyModel.object.aggregate(结果变量名=聚合函数("列"))
返回结果：结果变量名和值组成的字典
格式为：
    {
    "结果变量名":值
    }
"""

b1 = Book.objects.aggregate(avg_privce=Avg('book_price'), market_price=Avg('book_market_price'), )
print(b1)

"""
分组聚合

语法：QuerySet.annotate(结果变量名=聚合函数("列"))
返回值：QuerySet  
步骤：
    1.先用查询结果MyModel.object.values查找查询要分组聚合的列
        MyModel.object.values('列1','列2')
    2.通过返回结果的QuerySet.annotate方法分组聚合得到分组结果
        QuerySet.annotate(结果变量名=聚合函数("列"))
"""
b2 = Book.objects.values('author_id', )
b2_ = b2.annotate(auth_count=Count('author_id'))
print(b2_)
