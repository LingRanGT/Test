# Create your models here.

from django.db import models
from stdimage.models import StdImageField
from django.utils.safestring import mark_safe
#用户表
class User(models.Model):
    username = models.CharField(verbose_name='用户名',unique=True, max_length=64)
    head_img = StdImageField(upload_to='path/to/', blank=True,delete_orphans=True,
                          verbose_name=u'url')

    class Meta:
        db_table = 'user_info'
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'


    def get_image_tag(self):
        if self.head_img:
            return mark_safe('<img src="%s" width="60" height="75" />' % self.head_img.url)
        else:
            return ' '

    get_image_tag.short_description = 'Photo'
    # get_image_tag.allow_tags = True #redundant
    get_image_tag.admin_order_field = 'name'

    def __str__(self):
        return self.username



