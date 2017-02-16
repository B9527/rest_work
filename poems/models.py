# coding:utf-8
from django.db import models


# Create your models here.
class Poet(models.Model):
    name = models.CharField(max_length=20,verbose_name='姓名',null=False)
    dynasty = models.CharField(max_length=20,verbose_name='朝代',null=True)
    brief = models.CharField(max_length=250,verbose_name='简介',null=True)
    alias = models.CharField(max_length=20,verbose_name='称号',null=True)

    def __unicode__(self):
        return self.name


class Poem(models.Model):
    author = models.ForeignKey(Poet,null=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=250)
    type = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
