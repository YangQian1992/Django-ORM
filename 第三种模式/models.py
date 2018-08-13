from django.db import models

# Django ORM 中的多对多的三种模式之一：自定制创建第三张表，并在ManyToManyField中通过through和through_fields指定表名和字段

class Book(models.Model):
    title = models.CharField(max_length=32,verbose_name='书名')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=32,verbose_name='作者姓名')
    books = models.ManyToManyField(
        to='Book',
        through='Author2Book',
        through_fields=('author','book')    # 元组中第一个元素是对应着建立多对多字段的表
    )

    def __str__(self):
        return self.name

class Author2Book(models.Model):
    '''
    自定制多对多的第三张表
    '''
    book = models.ForeignKey(to='Book')
    author = models.ForeignKey(to='Author')

    class Meta:
        unique_together = (
            ('book','author'),  # 联合唯一
        )


# 自定制创建第三张表，并在ManyToManyField中通过through和through_fields指定表名和字段的优势：
#   一、可以扩展第三张关系表的字段（婚恋网站的男女用户的约会记录）

#   二、可以使用ORM提供的部分快捷方法：all()

