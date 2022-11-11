from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import SolutionModel


# Register your models here.
@admin.register(SolutionModel)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('picture', 'title', 'source', 'created_time', 'updated_time', 'pro_status')
    list_display_links = ('title',)
    list_filter = ('title', 'source', 'created_time', 'updated_time', 'pro_status')
    list_editable = ('source', 'pro_status')
    list_per_page = 20

    @admin.display(description='头像', ordering='name')
    def img(self, obj):
        div = f"<img src='{obj.icon.url}' width='32px'>"
        return mark_safe(div)