from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class User(admin.ModelAdmin):
    # 设置页面可以展示的字段
    list_display = ('username', 'head_img','get_image_tag')
    # 默认不配置的话，第一个字段会存在链接到记录编辑页面
    # list_display_links = None
    list_display_links = ('username',)