from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
import django.utils.timezone as timezone

# Create your models here.
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from stdimage import StdImageField


class SolutionModel(models.Model):
    picture = StdImageField('图片路径',upload_to='path/to/', blank=True,delete_orphans=True)
    title = models.CharField('标题', max_length=64, blank=False)
    list_url = models.CharField('URL', max_length=64, blank=True)
    source = models.CharField('来源', max_length=32, blank=False)
    content = RichTextUploadingField(default="")
    created_time = models.DateTimeField('创建时间', auto_now_add=True)  # 创建时间
    updated_time = models.DateTimeField('更新时间', auto_now=True)  # 更新时间
    pro_status = models.CharField('发布状态', max_length=1, default='Y')  # 发布状态 Y:发布；N:开发

    class Meta:
        db_table = 'tb_solution'
        verbose_name = "方案列表"
        verbose_name_plural = verbose_name

    # 在后台列表显示图片
    def get_image_tag(self):
        if self.picture:
            return mark_safe('<img src="%s" width="75" height="60" />' % self.picture.url)
        else:
            return ' '

    get_image_tag.short_description = 'Photo'
    get_image_tag.admin_order_field = 'name'

    def __str__(self):
        return self.title
