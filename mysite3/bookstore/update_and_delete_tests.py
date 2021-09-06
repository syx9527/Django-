from django.test import TestCase
from bookstore.models import Author, Book

# # 单个更新
# b1 = Book.objects.get(book_id=2021001)
# b1.book_price = 22
#
# b1.save()
# """************************************"""
# # 批量更新
# b2 = Book.objects.filter(book_price__gt=30)
# b2.update(book_price=45.5)
#
# # 更新所有
# b3 = Book.objects.all()
# b3.update(book_market_price=3.0)

# 删除
# b4 = Book.objects.filter(book_name='删除')
# b4.delete()

# 伪删除
# 添加一个布尔型字段is_active,默认为True，执行删除时将该字段设置为False
