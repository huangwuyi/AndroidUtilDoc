from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import Chapter, ChapterItem, ItemMethod, MethodParameter, MethodResult, SomeTangshi
from django.template import loader
from django.views import generic

# Create your views here.
projectName = "AndroidUtil"


def hello_android_util(request):
    return render(request, "helloAndroidUtil/HelloAndroidUtil.html", {"projectName": projectName, \
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


def chapter_item_method(request, chapter_lsno, item_lsno):
    chapter = Chapter.objects.get(chapter_lsno=chapter_lsno)
    chapter_item = ChapterItem.objects.get(id=item_lsno)
    # item_method_list = ItemMethod.objects.filter(chapter_item_id=chapter_item.id)
    item_method_list = ItemMethod.objects.filter(chapter_item=chapter_item)

    for item_method in item_method_list:
        item_method.parameters = MethodParameter.objects.filter(itemMethod_id=item_method.id)
        try:
            item_method.method_result = MethodResult.objects.get(item_method_id=item_method.id)
        except:
            item_method.method_result = {"result_type": "尚未维护", "result_descripe": "尚未维护"}
    return render(request, "helloAndroidUtil/chapter_item_detail.html", {"chapter_item": chapter_item, \
                                                                         "item_method_list": item_method_list, \
                                                                         "chapter": chapter})


def tang_list(request):
    sometangshi = SomeTangshi.objects.all()
    return render(request, "helloAndroidUtil/tang_list.html", {"tang_list": sometangshi})


def tang_item(request, id):
    tang = SomeTangshi.objects.get(id=id)
    return render(request, "helloAndroidUtil/tang_item.html", {"tang": tang})


# 一下两个方法仅仅是一个尝试  失败了最终
class IndexView(generic.ListView):
    template_name = 'helloAndroidUtil/chapter_index.html'
    context_object_name = 'chapters_list'
    queryset = Chapter.objects.all()


class DetaiView(generic.DetailView):
    template_name = "helloAndroidUtil/chapter_detail.html"
    model = Chapter
