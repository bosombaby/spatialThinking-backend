from django.db import models
from django.contrib.auth.models import AbstractUser


# 用户表
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=128, default='用户111')
    membership_level = models.IntegerField(default=0)
    gold_count = models.IntegerField(default=0)

# # 角色表
# class Role(models.Model):
