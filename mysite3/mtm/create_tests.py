from django.test import TestCase

# Create your tests here.
from .models import *

# 方案一，先创建author再关联book
a1 = Author.objects.create(name="吕老师")
a2 = Author.objects.create(name="王老师")
# 吕老师和王老师同时写了一本python
b1 = a1.book_set.create(title="Python")
a2.book_set.add(b1)

# 方案二，先创建book，再管理author

b2 = Book.objects.create(title="Python1")
# 张三和率老师都参与了Python1的创作
a3 = b2.author.create(name="张三")

b2.author.add(a1)
