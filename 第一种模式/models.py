from django.db import models

# Django ORM 中的多对多的三种模式之一：使用默认的MangToManyField创建第三张表

class Book(models.Model):
    title = models.CharField(max_length=32,verbose_name='书名')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=32,verbose_name='作者姓名')
    books = models.ManyToManyField(to='Book')

    def __str__(self):
        return self.name


# 使用默认的ManyToManyField创建第三张表的优势：
#     可以使用ORM提供的快捷方法：
#           1、add()
#           2、clear()
#           3、set()
#           4、remove()
#           5、all()

# 使用默认的ManyToManyField创建第三张表的劣势：
#     不能扩展第三张表的字段
