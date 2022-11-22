from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import SolutionModel


# Register your models here.
@admin.register(SolutionModel)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('get_image_tag', 'picture', 'title', 'source', 'created_time', 'updated_time', 'pro_status')
    list_display_links = ('title',)
    list_filter = ('title', 'source', 'created_time', 'updated_time', 'pro_status')
    list_editable = ('source', 'pro_status')
    list_per_page = 20
