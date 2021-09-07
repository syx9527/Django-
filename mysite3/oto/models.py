from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField("姓名", max_length=11)


class Wife(models.Model):
    name = models.CharField("姓名", max_length=11)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Classes(models.Model):
    name = models.CharField("科目名称", max_length=11)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
