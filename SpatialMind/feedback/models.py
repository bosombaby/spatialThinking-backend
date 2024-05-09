from django.db import models
from levels.models import Level
from django.contrib.auth.models import User


# 评分标准表，与闯关记录表进行多对多关联
class Scoring(models.Model):
    class Meta:
        verbose_name = "评分标准"
        verbose_name_plural = "评分标准 Scoring"

    scoring_id = models.AutoField(primary_key=True, verbose_name="评分ID")
    level = models.CharField(max_length=50, verbose_name="等级")
    score_range = models.CharField(max_length=50,default="90-100",  verbose_name="分数区间")
    description = models.CharField(max_length=128, verbose_name="描述")
    details = models.TextField(default="", null=True, blank=True, verbose_name="详情")

    def __str__(self):
        return self.level


# 闯关记录表，与用户表和关卡表进行一对一关联
class ChallengeRecord(models.Model):
    class Meta:
        verbose_name = "闯关记录"
        verbose_name_plural = "闯关记录 ChallengeRecord"

    record_id = models.AutoField(primary_key=True, verbose_name="闯关记录ID")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name="关卡")
    start_time = models.DateTimeField(auto_now_add=True, verbose_name="开始时间")
    end_time = models.DateTimeField(auto_now=True, verbose_name="结束时间")
    result = models.CharField(max_length=50, default="未完成", verbose_name="闯关结果")
    score = models.IntegerField(default=0, verbose_name="得分")
    scoring_standard = models.ManyToManyField(Scoring, verbose_name="评分标准")

    def __str__(self):
        return f"{self.user.username} 的 {self.level.level_name} 闯关记录"
