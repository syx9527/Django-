from django.test import TestCase

# Create your tests here.
from .models import *

# author1 = Author.objects.create(name='李老师')
# 插入数据时两种关联
# wife1 = Wife.objects.create(name='李夫人', author=author1)
# wife1 = Wife.objects.create(name='李夫人', author_id=1)


# 正向查询
w1 = Wife.objects.get(name='王夫人')
print(w1.name, '的老公是：', w1.author.name)

# 反向查询

a1 = Author.objects.get(name='王老师')

print(a1.classes.name)
