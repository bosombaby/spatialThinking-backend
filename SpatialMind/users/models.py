from django.db import models
from django.contrib.auth.models import User


# 角色表
class Role(models.Model):
    class Meta:
        verbose_name = "角色管理"
        verbose_name_plural = "角色管理 Role"

    role_id = models.AutoField(primary_key=True, verbose_name="角色ID")
    name = models.CharField(max_length=64, default='common', verbose_name="用户类型")
    permission_module = models.CharField(max_length=128, default='default', verbose_name='权限模块')

    def __str__(self):
        return f"{self.role_id} --- {self.permission_module}"


# 用户信息表
class Profile(models.Model):
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息 Profile"

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    nickname = models.CharField(max_length=100, default='默认用户', verbose_name='昵称')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="头像")
    membership_level = models.CharField(max_length=50, default="普通", verbose_name="会员等级")
    gold_count = models.IntegerField(default=0, verbose_name="金币数")
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="角色")

    def __str__(self):
        return f"{self.user.username} 用户信息"
