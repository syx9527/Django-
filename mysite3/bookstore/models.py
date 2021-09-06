from copy import copy

from django.db import models


# Create your models here.
class Author(models.Model):
    author_id = models.IntegerField("作者ID", primary_key=True)
    author_name = models.CharField("姓名", max_length=11)
    author_age = models.IntegerField("年龄", default=1)
    author_email = models.EmailField("邮箱", null=True)
    is_active = models.BooleanField('是否活跃', default=True)

    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = '作者'

    def __str__(self):
        return self.author_name


class Book(models.Model):
    # 数据库
    book_id = models.IntegerField('书号', primary_key=True, )
    book_name = models.CharField('书名', max_length=50, default='', null=True, unique=True)
    book_price = models.DecimalField("价格", max_digits=7, decimal_places=2, null=True)
    book_market_price = models.DecimalField("零价格", max_digits=7, decimal_places=2, null=True)
    book_info = models.CharField('描述', max_length=100, default='', null=True)

    # author_id = models.IntegerField("作者ID", null=True)
    # 设置外键
    author = models.OneToOneField(Author, on_delete=models.CASCADE, null=True)
    # models.CASCADE,级联删除，模拟SQL约束 ON DELETE CASCADE
    # models.PROTECT,抛出ProtectedError以组织被引用对象的删除
    # SET_NULL,设置ForeignKey null;需指定null=True
    # SET_DEFAULT,将ForeignKey设置为其默认值；必须设置ForeignKey的默认值

    pub = models.CharField("出版社", max_length=50, default='')
    is_active = models.BooleanField('是否活跃', default=True)

    class Meta:
        # 数据表名称，设置万需要立马更新同步数据库
        db_table = "book"
        # 给模型对象的一个易于理解的名称（单数），用于显示在/admin管理界面中
        verbose_name = '图书'
        # 该对象附属形式的名称（复数），用于显示在/admin管理界面
        verbose_name_plural = '图书'

    def __str__(self):
        return self.book_name
