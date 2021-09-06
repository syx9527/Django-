from django.contrib import admin

# Register your models here.
from .models import Book, Author


class BookManager(admin.ModelAdmin):
    # 首页展示列表
    list_display = ['book_name', "book_price", 'book_market_price', 'author_id', 'pub']
    # 列表中哪些可以点击进入编辑节面
    list_display_links = ['book_name', 'author_id', 'pub']
    # 过滤器
    list_filter = ['pub']
    # 搜索框
    search_fields = ['book_name']
    # 添加可在列表页编辑的字段
    list_editable = ["book_price", 'book_market_price', ]


class AuthorManager(admin.ModelAdmin):
    list_display = ['author_id', 'author_name', 'author_age', 'author_email']
    list_display_links = ['author_id', 'author_name', 'author_age', 'author_email']


# admin.site.register(Book)
admin.site.register(Book, BookManager)
admin.site.register(Author, AuthorManager)
