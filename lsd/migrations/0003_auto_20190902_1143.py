# Generated by Django 2.1.4 on 2019-09-02 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lsd', '0002_auto_20190902_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telephone',
            field=models.CharField(max_length=20, null=True, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='project',
            name='telephone',
            field=models.CharField(max_length=20, verbose_name='联系电话'),
        ),
    ]