from django.db import models


class UserInfo(models.Model):
    '''
    用户信息表
    '''
    GENDER = (
        (1, '男'),
        (0, '女'),
        (2, '未知'),
    )
    USER_STATUS = (
        (0, '未验证'),
        (1, '已激活'),
    )
    USER_SRC = (
        (1, '微博授权用户'),
        (2, '游客用户'),
        (3, '普通用户'),
        (4, '机构用户'),
    )
    username = models.CharField(max_length=20, help_text='用户姓名')
    password = models.CharField(max_length=20,help_text='用户密码')
    sex = models.IntegerField(choices=GENDER,default=2,help_text='用户性别')
    age = models.IntegerField(default=0, help_text='用户年龄')
    head = models.CharField(max_length=200, default='http://img95.699pic.com/photo/40027/3434.jpg_wh300.jpg',help_text='头像字段')
    email = models.CharField(max_length=50, help_text='用户邮箱')
    status = models.IntegerField(choices=USER_STATUS,default=0,help_text='邮箱验证状态')
    phone = models.CharField(max_length=11, help_text='用户手机号')
    card = models.CharField(max_length=18, help_text='用户身份证')
    school = models.CharField(max_length=20, help_text='所属院校')
    src = models.IntegerField(choices=USER_SRC,default=2,help_text='用户类别')

