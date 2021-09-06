from django.db.models import F, Q
from django.test import TestCase
from bookstore.models import Author, Book

# F 对象
# 操作
# 高并发，
# b1 = Book.objects.all()
# b1.update(book_market_price=F('book_market_price') * 0.75)

# 取出零售价大于标价的书本
b2 = Book.objects.filter(book_market_price__gt=F('book_price'), is_active=True)
print(b2)

# Q对象，与、或、非等

#  Q(条件1) | Q(条件2)      条件1成立或者条件2成立
#  Q(条件1) & | Q(条件2)      条件1和条件2同时成立
#  Q(条件1) & ~ Q(条件2)      条件1成立且条件2不成立

# 取出名字中含有"测试"两个字但是作者标号不为 100002 的书本
b3 = Book.objects.filter(Q(book_name__contains="测试") & ~ Q(author_id=100002))
print(b3.values())
