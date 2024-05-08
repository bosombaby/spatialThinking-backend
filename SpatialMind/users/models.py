from django.db import models
from django.contrib.auth.models import User


# 用户表
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=128, default='空间思维')
    membership_level = models.IntegerField(default=0)
    gold_count = models.IntegerField(default=0)

# # 角色表
# class Role(models.Model):
