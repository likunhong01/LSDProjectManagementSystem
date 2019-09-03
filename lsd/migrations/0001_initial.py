# Generated by Django 2.1.4 on 2019-09-01 09:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='留言id')),
                ('read', models.IntegerField(default=0, verbose_name='是否已读')),
                ('effective', models.IntegerField(default=0, verbose_name='是否有效')),
                ('time', models.DateField(default=django.utils.timezone.now, verbose_name='时间')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='项目id，自增')),
                ('project_name', models.CharField(max_length=20, verbose_name='项目名称')),
                ('source', models.CharField(max_length=30, verbose_name='项目来源')),
                ('contacts', models.CharField(max_length=20, verbose_name='对方联系人')),
                ('telephone', models.CharField(max_length=20, verbose_name='联系对话')),
                ('introduction', models.CharField(max_length=256, verbose_name='项目简介')),
                ('time', models.DateField(default=django.utils.timezone.now, verbose_name='时间')),
                ('effective', models.IntegerField(default=0, verbose_name='是否有效')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='汇报记录id')),
                ('reporter', models.CharField(max_length=20, verbose_name='汇报人')),
                ('capital', models.CharField(max_length=256, verbose_name='资金情况')),
                ('workable', models.CharField(max_length=1024, verbose_name='落实情况')),
                ('invoice', models.CharField(max_length=256, verbose_name='开票情况')),
                ('progress', models.CharField(max_length=1024, verbose_name='项目进展')),
                ('other', models.CharField(max_length=1024, verbose_name='其它')),
                ('effective', models.IntegerField(default=0, verbose_name='是否有效')),
                ('time', models.DateField(default=django.utils.timezone.now, verbose_name='时间')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lsd.Project', verbose_name='项目id')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='用户id,自增')),
                ('user_name', models.CharField(max_length=255, verbose_name='用户名即真实姓名')),
                ('password', models.CharField(max_length=20, verbose_name='密码+MD5加密')),
                ('authority', models.CharField(max_length=20, verbose_name='权限')),
            ],
        ),
        migrations.CreateModel(
            name='UserProject',
            fields=[
                ('userProject_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='主键')),
                ('pro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lsd.Project')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lsd.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserStr',
            fields=[
                ('userStr_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='主键')),
                ('str', models.CharField(max_length=10, verbose_name='加密字符串')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lsd.User')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='report_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lsd.Report', verbose_name='回报记录id'),
        ),
    ]