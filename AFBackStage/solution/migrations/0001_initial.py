# Generated by Django 4.0.3 on 2022-11-11 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolutionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='icon/', verbose_name='图片')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('list_url', models.CharField(blank=True, max_length=64, verbose_name='URL')),
                ('source', models.CharField(max_length=32, verbose_name='来源')),
                ('content', models.TextField(verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('pro_status', models.CharField(default='N', max_length=1, verbose_name='发布状态')),
            ],
            options={
                'verbose_name': '方案列表',
                'verbose_name_plural': '方案列表',
                'db_table': 'tb_solution',
            },
        ),
    ]