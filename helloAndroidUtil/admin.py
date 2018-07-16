from django.contrib import admin

# Register your models here.
from .models import Chapter, ChapterItem, ItemMethod, MethodParameter

# 通过再次注册模型，Django能够快速构建一个默认的表单用于展示。

admin.site.register(ChapterItem)
admin.site.register(ItemMethod)
admin.site.register(MethodParameter)


class ChapterAdmin(admin.ModelAdmin):
    # fields = ['章节名称', { ('chapter_name')}, ('章节序号', {'chapter_lsno'}), ]
    fieldsets = [('章节名称', {  'fields': ['chapter_name','chapter_descripe']}),
                 ('章节序号', {  'fields': ['chapter_lsno']})
                 ]


admin.site.register(Chapter, ChapterAdmin)
