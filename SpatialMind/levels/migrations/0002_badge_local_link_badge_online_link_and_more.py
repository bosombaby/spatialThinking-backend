# Generated by Django 4.2.11 on 2024-05-09 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='local_link',
            field=models.FileField(null=True, upload_to='badges/', verbose_name='本地链接'),
        ),
        migrations.AddField(
            model_name='badge',
            name='online_link',
            field=models.URLField(null=True, verbose_name='线上链接'),
        ),
        migrations.AlterField(
            model_name='badge',
            name='content',
            field=models.TextField(default='', null=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='badge',
            name='description',
            field=models.TextField(default='', null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='learning_modules',
            field=models.TextField(default='', null=True, verbose_name='学习模块'),
        ),
    ]
