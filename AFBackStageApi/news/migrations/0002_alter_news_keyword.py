# Generated by Django 4.0.3 on 2022-11-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='keyword',
            field=models.CharField(blank=True, max_length=16, verbose_name='关键字'),
        ),
    ]
