from django.contrib import admin

# Register your models here.
from .models import  Chapter,ChapterItem,ItemMethod

admin.site.register(Chapter)
admin.site.register(ChapterItem)
admin.site.register(ItemMethod)