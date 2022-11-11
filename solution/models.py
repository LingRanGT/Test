from django.db import models
import django.utils.timezone as timezone


# Create your models here.
from django.utils.html import format_html
from stdimage import StdImageField


class SolutionModel(models.Model):
    # picture = StdImageField(upload_to='icon/', blank=True, delete_orphans=True, variations={'thumbnail': (100, 75)}, verbose_name=u'url'),
    picture = models.ImageField('图片', upload_to='icon/')
    title = models.CharField('标题', max_length=64, blank=False)
    list_url = models.CharField('URL', max_length=64, blank=True)
    source = models.CharField('来源', max_length=32, blank=False)
    content = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)  # 创建时间
    updated_time = models.DateTimeField('更新时间', auto_now=True)  # 更新时间
    pro_status = models.CharField('发布状态', max_length=1, default='N')  # 发布状态 Y:发布；N:开发

    class Meta:
        db_table = 'tb_solution'
        verbose_name = "方案列表"
        verbose_name_plural = verbose_name

    # 这里要使用format_html 才可以在后台显示图片
    # def image_img(self):
    #     return format_html(
    #         '<img src="{}" width="100px"/>',
    #         self.head_img.thumbnail.url,
    #     )

    # image_img.short_description = '图片'
    # 图片是否显示
    # image_img.allow_tags = True

    def __str__(self):
        return self.title
