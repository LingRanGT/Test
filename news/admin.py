from django.contrib import admin
from .models import News

# Register your models here.

admin.site.site_header = '管理后台'  # 设置header
admin.site.site_title = '管理后台'  # 设置title
# admin.site.index_title = '管理后台'


@admin.register(News)
class News(admin.ModelAdmin):
    # 设置页面可以展示的字段
    list_display = ('title', 'keyword', 'source', 'created_time', 'updated_time', 'pro_status')
    # 默认不配置的话，第一个字段会存在链接到记录编辑页面
    # list_display_links = None
    list_display_links = ('title',)
    # 设置过滤选项
    list_filter = ('title', 'keyword', 'source', 'created_time', 'updated_time', 'pro_status')
    # 设置可编辑字段 如果设置了可以编辑字段，页面会自动增加保存按钮
    list_editable = ('keyword', 'source','pro_status')
    # 每页显示条目数 缺省值100
    list_per_page = 20