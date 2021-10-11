from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import UserInfo, Blog, Category, Tag, Article2Tag, Article, ArticleUpDown, Comment


class BlogModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('title')


admin.site.register(UserInfo)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article2Tag)
admin.site.register(Article)
admin.site.register(ArticleUpDown)
admin.site.register(Comment)
# Register your models here.
