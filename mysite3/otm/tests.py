from django.test import TestCase
from .models import *

# Create your tests here.
# 一对多

# p1 = Publisher.objects.create(name='人民出版社')
# # p1 = Publisher.objects.get(id=2).delete()
#
# # 根据外键创建数据的两种方式
# Book.objects.create(title="python入门到精通", publisher=p1)
# Book.objects.create(title="Python数据结构", publisher=p1)


# 正向查询
b1 = Book.objects.get(id=3)
print(b1.title, "出版社为：", b1.publisher.name)

# 反向查询
p2 = Publisher.objects.get(name="清华大学")
w2 = p2.book_set.all()
print(p2.name, "出版的书有")
for i in w2:
    print(i.title)
