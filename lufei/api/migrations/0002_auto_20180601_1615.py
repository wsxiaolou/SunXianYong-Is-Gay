# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-01 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='标题')),
                ('article_type', models.SmallIntegerField(choices=[(0, '资讯'), (1, '视频')], default=0)),
                ('brief', models.TextField(max_length=512, verbose_name='摘要')),
                ('head_img', models.CharField(max_length=255)),
                ('content', models.TextField(verbose_name='文章正文')),
                ('pub_date', models.DateTimeField(verbose_name='上架日期')),
                ('offline_date', models.DateTimeField(verbose_name='下架日期')),
                ('status', models.SmallIntegerField(choices=[(0, '在线'), (1, '下线')], default=0, verbose_name='状态')),
                ('order', models.SmallIntegerField(default=0, help_text='文章想置顶，可以把数字调大，不要超过1000', verbose_name='权重')),
                ('vid', models.CharField(blank=True, help_text='文章类型是视频, 则需要添加视频VID', max_length=128, null=True, verbose_name='视频VID')),
                ('comment_num', models.SmallIntegerField(default=0, verbose_name='评论数')),
                ('agree_num', models.SmallIntegerField(default=0, verbose_name='点赞数')),
                ('view_num', models.SmallIntegerField(default=0, verbose_name='观看数')),
                ('collect_num', models.SmallIntegerField(default=0, verbose_name='收藏数')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('position', models.SmallIntegerField(choices=[(0, '信息流'), (1, 'banner大图'), (2, 'banner小图')], default=0, verbose_name='位置')),
            ],
            options={
                'verbose_name_plural': '17. 文章',
            },
        ),
        migrations.CreateModel(
            name='ArticleSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name_plural': '16. 文章来源',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Account')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': '18. 通用收藏表',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content', models.TextField(max_length=1024)),
                ('disagree_number', models.IntegerField(default=0, verbose_name='踩')),
                ('agree_number', models.IntegerField(default=0, verbose_name='赞同数')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Account', verbose_name='会员名')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='类型')),
                ('p_node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Comment', verbose_name='父级评论')),
            ],
            options={
                'verbose_name_plural': '19. 通用评论表',
            },
        ),
        migrations.CreateModel(
            name='UserAuthToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Account')),
            ],
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='course',
        ),
        migrations.RemoveField(
            model_name='usertoken',
            name='user',
        ),
        migrations.DeleteModel(
            name='Chapter',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
        migrations.DeleteModel(
            name='UserToken',
        ),
        migrations.AddField(
            model_name='article',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ArticleSource', verbose_name='来源'),
        ),
        migrations.AlterUniqueTogether(
            name='collection',
            unique_together=set([('content_type', 'object_id', 'account')]),
        ),
    ]
