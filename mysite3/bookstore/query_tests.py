from django.test import TestCase
from bookstore.models import Author, Book

# 返回值为对象
authors = Author.objects.all()
print(authors)
"""
<QuerySet [<Author: 作者1>, <Author: 作者2>]>
"""
for author in authors:
    print(author)
"""
作者1
作者2
"""
print('- ' * 8)

# 返回值为字典
b1 = Book.objects.values('book_name', 'book_price', 'pub')
for book in b1:
    print(book, end="  ")
    print(book['book_name'])
"""
{'book_name': 'python学习', 'book_price': Decimal('11.20'), 'pub': '人民出版社 '}   python学习
{'book_name': '测试书籍2', 'book_price': Decimal('52.30'), 'pub': '测试出版社'}   测试书籍2
{'book_name': '测试书籍3', 'book_price': Decimal('35.60'), 'pub': '出版社测试3'}   测试书籍3
"""
print('- ' * 8)

# 返回值为元组
b2 = Book.objects.values_list('book_name', 'book_price', 'pub')
print(b2)
"""
<QuerySet [('python学习', Decimal('11.20'), '人民出版社 '), ('测试书籍2', Decimal('52.30'), '测试出版社'), ('测试书籍3', Decimal('35.60'), '出版社测试3')]>
"""
for book in b2:
    print(book)
"""
('python学习', Decimal('11.20'), '人民出版社 ')
('测试书籍2', Decimal('52.30'), '测试出版社')
('测试书籍3', Decimal('35.60'), '出版社测试3')
"""
print('- ' * 8)

# 查询结果排序

b3 = Book.objects.order_by('book_id')
for book in b3:
    print(book.book_name, book.book_id, book.author_id, book.pub)
"""
python学习 2021001 100001 人民出版社 
测试书籍2 2021002 100002 测试出版社
测试书籍3 2021003 10001 出版社测试3
"""
print("* " * 8)
b3 = Book.objects.values('book_name', 'book_id', 'author_id', 'pub').order_by('author_id')
print(b3.query, end="\n\n")
for book in b3:
    print(book)
    # print(book.book_name, book.book_id, book.author_id, book.pub)
"""
测试书籍3 2021003 10001 出版社测试3
测试书籍2 2021002 100002 测试出版社
python学习 2021001 100001 人民出版社
"""
print('- ' * 8)

# 条件查询
# 1.filter(条件)，返回满足所有条件的全部数据集

b4 = Book.objects.filter(author_id="100001")
print(b4)
"""
<QuerySet [<Book: python学习>, <Book: 测试书籍3>]>
"""

for book in b4:
    print(book.book_name, book.author_id, book.pub)
"""
<QuerySet [<Book: python学习>, <Book: 测试书籍3>]>
"""
print('* ' * 8)

# 2.exclude(条件)，返回不满足所有条件的全部数据集
b5 = Book.objects.exclude(author_id="100001")
print(b5)
"""
<QuerySet [<Book: 测试书籍2>]>
"""

for book in b5:
    print(book.book_name, book.author_id, book.pub)
"""
测试书籍2 100002 测试出版社2
"""
print('* ' * 8)
# 3.get(条件),
# 返回满足条件的唯一一条数据,查询结果多于一条则抛出Model.MultipleObjectsReturned异常，如果没有数据则抛出Model.DoesNotExist异常
b5 = Book.objects.get(book_id="2021001")
print(b5.book_name, b5.book_id)
"""
python学习 2021001
"""

print('- ' * 8)

# 非等式查询，例如,price > 5
# 查询谓词

# 1. __exact:等值匹配

a1 = Author.objects.filter(author_id__exact=100001)
print(a1)
"""
python学习 2021001
"""
for author in a1:
    print(author.author_id, author.author_name, author.author_age)
"""
100001 作者1 23
"""
print('* ' * 8)

# 2. __contains:包含指定值
a3 = Author.objects.filter(author_name__contains='测试')
for author in a3:
    print(author.author_id, author.author_name, author.author_age)
"""
100003 测试作者1 30
100004 测试作者2 14
"""
# 3. __startwith:    以XXX开始
# 4. __endwith:      以XXX结束

print('* ' * 8)
# 5. __gt:  大于指定值
a4 = Author.objects.filter(author_age__gt=25)
for author in a4:
    print(author.author_id, author.author_name, author.author_age)
"""
100002 作者2 40
100003 测试作者1 30
"""

# 6. __gte:大于等于
# 7. __lt:小于
# 8. __lte:小于等于

print('- ' * 8)

# 9. __in:查找数据是否在指定范围内
a5 = Author.objects.filter(author_name__in=['作者1', '作者2'])
for author in a5:
    print(author.author_id, author.author_name, author.author_age)
"""
100001 作者1 23
100002 作者2 40
"""
print('- ' * 8)

# 10. __range:查找数据是否在指定的区间范围内
a6 = Author.objects.filter(author_age__range=(20, 35)).order_by('-author_age')
print(a6.query)
for author in a6:
    print(author.author_id, author.author_name, author.author_age)
"""
100001 作者1 23
100003 测试作者1 30
"""
print('- ' * 8)
