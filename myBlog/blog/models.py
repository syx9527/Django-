from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserInfo(AbstractUser):
    """用户信息"""
    nid = models.AutoField(primary_key=True, )
    telephone = models.CharField(max_length=11, null=True, unique=True, )
    # 存储用户头像文件
    avatar = models.FileField(upload_to='avatars/', default="avatars/default.png")
    # 在生成字段时就以当前时间存储，用于计算园龄
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 业务分离,用户名下blog删除，则站点blog同时删除
    blog = models.OneToOneField(to='Blog', to_field='nid', null=True, on_delete=models.PROTECT,
                                related_name="UserInfo_blog")

    def __str__(self):
        return self.username


class Blog(models.Model):
    """
    博客信息表---站点表
    1. 直接继承自UserInfo的nid，同时拒绝删除外键，设置自增减
    """
    # nid = models.OneToOneField(to='UserInfo', to_field='nid', on_delete=models.PROTECT, parent_link=True, primary_key=True,
    #                            related_name='Blog_nid')
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='个人博客标题', max_length=64)
    # https://home.cnblogs.com/u/1915559/，对应这部分[u/1915559/]
    site_name = models.CharField(verbose_name='站点名称', max_length=64)
    # 一套CSS文件
    theme = models.CharField(verbose_name='博客主题', max_length=32)

    def __str__(self):
        return self.title


class Category(models.Model):
    """博主个人文章分类表"""
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='分类标题', max_length=32)
    # 分类表下的blog删除之后，整篇blog也会删除，因此设置级联删除
    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid', on_delete=models.CASCADE,
                             related_name='Category_blog', db_column='blog')

    def __str__(self):
        return self.title


class Tag(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标签名称', max_length=32)
    # on_delete=models.PROTECT 标签被删除，外键关联的blog不能被删除
    # to_field='nid' 关联对象的字段名称，该字段必须是unique=True
    # related_name 指定用于反向查询的对象, 如果两个对象继承自同一个类，重命名之后则不再因为反向查询而冲突
    # 标签表下的blog删除之后，整篇blog也会删除，因此设置级联删除
    blog_id = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid', on_delete=models.CASCADE,
                                related_name='Article', db_column='blog_nid')

    def __str__(self):
        return self.title


class Article(models.Model):
    """
    文章表
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='文章标题')
    # desc 是description---摘要
    desc = models.CharField(max_length=255, verbose_name='文章描述')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    comment_count = models.IntegerField(default=0)
    up_count = models.IntegerField(default=0)
    down_count = models.IntegerField(default=0)

    # 文章表下的用户删除之后，原来的用户信息也会删除，因为文章表必须要有作者
    user = models.ForeignKey(verbose_name='作者', to='UserInfo', to_field='nid', on_delete=models.CASCADE,
                             related_name='Article_user', db_column='user')
    # 文章下对分类的删除也会对分类主表进行删除
    category = models.ForeignKey(verbose_name="文章分类",to='Category', to_field='nid', null=True, on_delete=models.CASCADE,
                                 related_name='Article_category', db_column='category')
    tags = models.ManyToManyField(

        to="Tag",  # to 参数用来指定与当前model类关联的model类
        through='Article2Tag',
        through_fields=('article', 'tag')
    )
    content = models.TextField(verbose_name="正文")

    def __str__(self):
        return self.title


class Article2Tag(models.Model):
    """
    文章表与标签表的中间表
    仅仅添加了一个新的ID，用于给两个表内容进行定位
    一旦文章表或者标签表删除，则与他们关联的ID则删除，称为级联删除
    """
    nid = models.AutoField(primary_key=True)
    # 标签和文章的关联，属于多对多关系，标签可以删除，表不能删除，所以外键关联
    # 中间表相当于对两张表的引用，因此删除也需要同步
    article = models.ForeignKey(verbose_name='文章', to="Article", to_field='nid', on_delete=models.CASCADE)
    tag = models.ForeignKey(verbose_name='标签', to="Tag", to_field='nid', on_delete=models.CASCADE)

    class Meta:
        # 联合唯一，字段不能重复
        unique_together = [
            ('article', 'tag'),
        ]

    def __str__(self):
        v = self.article.title + "---" + self.tag.title
        return v


class ArticleUpDown(models.Model):
    """
        点赞表
        如果点赞被删除，那么用户表和文件表不会被删除
    """
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to='UserInfo', null=True, on_delete=models.PROTECT)
    article = models.ForeignKey("Article", null=True, on_delete=models.PROTECT)
    is_up = models.BooleanField(default=True)

    class Meta:
        unique_together = [
            ('article', 'user')
        ]


class Comment(models.Model):
    """评论表"""
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(verbose_name='评论者', to='UserInfo', to_field='nid', on_delete=models.PROTECT)
    article = models.ForeignKey(verbose_name='评论文章', to='Article', to_field='nid', on_delete=models.PROTECT)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 富文本编辑器 ckeditor
    # body = RichTextField()
    content = models.CharField(verbose_name='评论内容', max_length=255)
    # self == Comment: 数据库语法自关联
    parent_comment = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


