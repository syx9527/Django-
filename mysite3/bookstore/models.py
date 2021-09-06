from django.db import models


# Create your models here.

class Book(models.Model):
    # 数据库
    book_id = models.IntegerField('书号', primary_key=True, )
    book_name = models.CharField('书名', max_length=50, default='', null=True, unique=True)
    book_price = models.DecimalField("价格", max_digits=7, decimal_places=2, null=True)
    book_market_price = models.DecimalField("零价格", max_digits=7, decimal_places=2, null=True)
    book_info = models.CharField('描述', max_length=100, default='', null=True)
    author_id = models.IntegerField("作者ID", null=True)
    pub = models.CharField("出版社", max_length=50, default='')
    is_active = models.BooleanField('是否活跃', default=True)

    class Meta:
        db_table = "book"

    def __str__(self):
        return self.book_name


class Author(models.Model):
    author_id = models.IntegerField("作者ID", primary_key=True)
    author_name = models.CharField("姓名", max_length=11)
    author_age = models.IntegerField("年龄", default=1)
    author_email = models.EmailField("邮箱", null=True)
    is_active = models.BooleanField('是否活跃', default=True)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.author_name
