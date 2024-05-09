from django.db import models


# 学科表
class Subject(models.Model):
    class Meta:
        verbose_name = "学科信息"
        verbose_name_plural = "学科信息 Subject"

    subject_id = models.AutoField(primary_key=True, verbose_name='学科 ID')
    subject_name = models.CharField(max_length=100, default="未命名学科", verbose_name="学科名")
    learning_modules = models.TextField(default="", null=True, verbose_name="学习模块")

    def __str__(self):
        return self.subject_name


# 勋章表，与关卡表进行一对多关联
class Badge(models.Model):
    class Meta:
        verbose_name = "勋章信息"
        verbose_name_plural = "勋章信息 Badge"

    badge_id = models.AutoField(primary_key=True, verbose_name="勋章ID")
    name = models.CharField(max_length=100, default="未命名勋章", verbose_name="名称")
    online_link = models.URLField(null=True, blank=True, verbose_name="线上链接")
    local_link = models.FileField(null=True, blank=True, upload_to='badges/', verbose_name="本地链接")
    description = models.TextField(default="", null=True, blank=True, verbose_name="描述")
    content = models.TextField(default="", null=True, blank=True, verbose_name="内容")
    acquired_count = models.IntegerField(default=0, verbose_name="获得人数")

    def __str__(self):
        return self.name


# 关卡表，与学科表进行多对一关联
class Level(models.Model):
    class Meta:
        verbose_name = "关卡信息"
        verbose_name_plural = "关卡信息 Level"

    level_id = models.AutoField(primary_key=True, verbose_name="关卡ID")
    level_name = models.CharField(max_length=100, default="未命名关卡", verbose_name="关卡名称")
    description = models.TextField(default="", verbose_name="描述")
    difficulty = models.CharField(max_length=50, default="简单", verbose_name="难度等级")
    score_range = models.CharField(max_length=50, default="0-100", verbose_name="分数区间")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="学科")
    badge = models.ForeignKey(Badge, on_delete=models.SET_NULL, null=True, blank=True, related_name='levels',
                              verbose_name="勋章")

    def __str__(self):
        return f"{self.subject} -- {self.level_name}"


# 题目表，与关卡表进行多对一关联
class Question(models.Model):
    class Meta:
        verbose_name = "题目信息"
        verbose_name_plural = "题目信息 Question"

    question_id = models.AutoField(primary_key=True, verbose_name="题目ID")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name="关卡")
    content = models.TextField(verbose_name="题目内容")
    # 添加选项字段，这里以四个选项为例
    option_a = models.CharField(max_length=200, default='', verbose_name="选项A")
    option_b = models.CharField(max_length=200, default='', verbose_name="选项B")
    option_c = models.CharField(max_length=200, null=True, blank=True, verbose_name="选项C")
    option_d = models.CharField(max_length=200, null=True, blank=True, verbose_name="选项D")
    answer = models.CharField(max_length=64, verbose_name="答案")
    solution = models.TextField(default='', verbose_name="解题思路")

    def __str__(self):
        return self.content
