from django.db import models


class OrganInfo(models.Model):
    '''
    机构分类表
    '''
    TYPE_CHOICES = (
        (1, '培训机构'),
        (2, '高校'),
        (3, '个人院校'),
        (4, '名校'),
    )
    name = models.CharField(max_length=20, help_text='机构名称')
    password = models.CharField(max_length=20, help_text='机构用户密码')
    head = models.CharField(max_length=200, default='http://img95.699pic.com/photo/40027/3434.jpg_wh300.jpg',
                            help_text='机构校标')
    desc = models.TextField(help_text='机构描述')
    email = models.CharField(max_length=20, help_text='机构邮箱')
    attn = models.CharField(max_length=20, help_text='联系人')
    phone = models.CharField(max_length=11, help_text='联系电话')
    site = models.TextField(help_text='机构地址')
    type = models.IntegerField(choices=TYPE_CHOICES, help_text='机构类型')


class Course(models.Model):
    '''
    课程分类表
    '''
    KIND_TYPES = (
        (1, '编程类'),
        (2, '系统类'),
        (3, '框架类'),
        (4, '数据库类'),
        (5, '文科类'),
        (6, '理科类'),
        (7, '体育类'),
        (8, '面试题类'),
    )
    organ_id = models.ForeignKey(OrganInfo, verbose_name='所属机构', on_delete=models.CASCADE)
    name = models.IntegerField(choices=KIND_TYPES, help_text='分类名称')
    head = models.CharField(max_length=200, default='http://img95.699pic.com/photo/40027/3434.jpg_wh300.jpg',
                            help_text='分类Logo')
    desc = models.TextField(help_text='分类描述')


