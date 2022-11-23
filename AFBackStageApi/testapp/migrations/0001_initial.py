# Generated by Django 4.0.3 on 2022-11-11 06:17

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='用户名')),
                ('head_img', stdimage.models.StdImageField(blank=True, force_min_size=False, upload_to='path/to/', variations={'thumbnail': (100, 75)}, verbose_name='url')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'user_info',
            },
        ),
    ]
