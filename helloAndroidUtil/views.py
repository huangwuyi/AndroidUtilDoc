from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import Chapter, ChapterItem, ItemMethod, MethonParameter
from django.template import loader

# Create your views here.
projectName = "AndroidUtil"


def hello_android_util(requset):
    return render(requset, "helloAndroidUtil/HelloAndroidUtil.html", {"projectName": projectName, \
                                                                      "timeSince": time.strftime("%y-%m-%d %H:%M:%S",
                                                                                                 time.gmtime())})


def chapter(request):
    chapter_list = Chapter.objects.all()
    template = loader.get_template('helloAndroidUtil/chapter_index.html')
    context = {
        'chapters_list': chapter_list
    }
    return HttpResponse(template.render(context, request))


def chapter_item(request, chapter_lsno):
    chapter = Chapter.objects.get(chapter_lsno=chapter_lsno)
    chapter_item_list = ChapterItem.objects.filter(chapter_id=chapter_lsno)
    return render(request, "helloAndroidUtil/chapter_detail.html",
                  {"chapter": chapter, "chapter_item_list": chapter_item_list})


def chapter_item_method(request, item_lsno):
    chapter_item = ChapterItem.objects.get(item_lsno=item_lsno)
    # item_method_list = ItemMethod.objects.filter(chapter_item_id=chapter_item.id)
    item_method_list = ItemMethod.objects.filter(chapter_item=chapter_item)
    for item_method in item_method_list:
        item_method.parameters = MethonParameter.objects.filter(itemMethod_id=item_method.id)
    return render(request, "helloAndroidUtil/chapter_item_detail.html", {"chapter_item": chapter_item,\
                                                                         "item_method_list": item_method_list})
