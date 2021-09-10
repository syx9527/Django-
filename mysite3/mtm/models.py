from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField("作者姓名", max_length=11)


class Book(models.Model):
    title = models.CharField("书名", max_length=11)
    author = models.ManyToManyField(Author)
