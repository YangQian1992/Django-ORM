from django.db import models

# Django ORM 中的多对多的三种模式之一：自定制创建第三张表

class Book(models.Model):
    title = models.CharField(max_length=32,verbose_name='书名')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=32,verbose_name='作者姓名')

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


# 使用自定制的第三张关系表的优势：
#   可以扩展第三张关系表的字段（婚恋网站的男女用户的约会记录）

# 使用自定制的第三张关系表的劣势：
#     不能使用ORM提供的快捷方法：
#           1、add()
#           2、clear()
#           3、set()
#           4、remove()
#           5、all()