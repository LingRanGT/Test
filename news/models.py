from django.db import models
import django.utils.timezone as timezone


# Create your models here.

class News(models.Model):
    title = models.CharField('标题', max_length=48, blank=False)
    keyword = models.CharField('关键字', max_length=16, blank=True)
    source = models.CharField('来源', max_length=16, blank=False)
    content = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)  # 创建时间
    updated_time = models.DateTimeField('更新时间', default=timezone.now)  # 更新时间
    pro_status = models.CharField('发布状态', max_length=1, default='N')  # 发布状态 Y:发布；N:开发

    class Meta:
        verbose_name = "新闻列表"
        verbose_name_plural = "新闻列表"

    def __str__(self):
        return self.title
