from django.db import models


# Create your models here.

class Content(models.Model):
    desc = models.CharField('标题', max_length=100, default='')
    myfile = models.FileField('文件', upload_to='picture')
