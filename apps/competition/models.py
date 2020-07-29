from django.db import models
from apps.business.models import Course
from apps.account.models import UserInfo


class BankInfo(models.Model):
    '''
    题库信息表
    '''
    course_id = models.ForeignKey(Course, verbose_name='所属分类', on_delete=models.CASCADE)
    name = models.CharField(max_length=20,help_text='题库名称')
    choices = models.CharField(max_length=5,help_text='选择题数')
    gaps = models.CharField(max_length=5,help_text='填空题数')
    judges = models.CharField(max_length=5,help_text='判断题数')
    num = models.CharField(max_length=5,help_text='此试卷使用次数')
    popnum = models.CharField(max_length=5,help_text='总答题人数')


class CourseDetailsInfo(models.Model):
    '''
    比赛信息表
    '''
    details_id = models.ForeignKey(BankInfo, verbose_name='比赛分类', on_delete=models.CASCADE)
    name = models.CharField(max_length=20,help_text='比赛名称')
    num = models.CharField(max_length=3,help_text='题目个数')
    start_time = models.TimeField(auto_now_add=True,help_text='开始时间')
    end_time = models.TimeField(auto_now_add=True,help_text='结束时间')
    answer = models.TimeField(auto_now_add=True,help_text='答题时间')
    total = models.CharField(max_length=3,help_text='总分')
    partnum = models.CharField(max_length=3,help_text='参与人数')


class choice(models.Model):
    '''
    选择题
    '''
    choice_id = models.ForeignKey(BankInfo, verbose_name='所属题库', on_delete=models.CASCADE)
    issue = models.CharField(max_length=200,help_text='题目内容')
    result = models.CharField(max_length=200,help_text='题目答案')
    A = models.CharField(max_length=200,help_text='选项内容')
    B = models.CharField(max_length=200,help_text='选项内容')
    C = models.CharField(max_length=200,help_text='选项内容')
    D = models.CharField(max_length=200,help_text='选项内容')


class gap(models.Model):
    '''
    判断题
    '''
    gap_id = models.ForeignKey(BankInfo, verbose_name='所属题库', on_delete=models.CASCADE)
    issue = models.CharField(max_length=200, help_text='题目内容')
    result = models.CharField(max_length=200, help_text='题目答案')
    true = models.CharField(max_length=200, help_text='选项内容')
    false = models.CharField(max_length=200, help_text='选项内容')


class judge(models.Model):
    '''
    填空题
    '''
    judge_id = models.ForeignKey(BankInfo, verbose_name='所属题库', on_delete=models.CASCADE)
    issue = models.CharField(max_length=200, help_text='题目内容')
    result = models.CharField(max_length=200, help_text='题目答案')


class record(models.Model):
    '''
    比赛信息记录表
    '''
    STATUS_CHOICES = (
        (1, '未完成'),
        (2, '已完成'),
        (3, '超时')
    )
    record_id = models.ForeignKey(BankInfo, verbose_name='所属题库', on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserInfo, verbose_name='所属用户', on_delete=models.CASCADE)
    state = models.IntegerField(choices=STATUS_CHOICES,help_text='答题状态')
    issue_record = models.TextField(help_text='题目记录')
    result_record = models.TextField(help_text='回答记录')
    start_time = models.TimeField(auto_now_add=True,help_text='开始时间')
    end_time = models.TimeField(auto_now_add=True,help_text='结束时间')
    answer = models.TimeField(auto_now_add=True,help_text='用时')
    true_num = models.CharField(max_length=3,help_text='正确数')
    false_num = models.CharField(max_length=3,help_text='错误数')
    goal = models.CharField(max_length=3,help_text='得分')


