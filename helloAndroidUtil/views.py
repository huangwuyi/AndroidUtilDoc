from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import Chapter
from django.template import loader

# Create your views here.
projectName = "AndroidUtil"


def hello_android_util(requset):
    return render(requset, "helloAndroidUtil/HelloAndroidUtil.html", {"projectName": projectName, \
                                                                      "timeSince": time.strftime("%y-%m-%d %H:%M:%S",
                                                                                                 time.gmtime())})


def chapter_item(request, chapter_lsno):
    return HttpResponse("you are looking at chapters:%s." % chapter_lsno)


def chapter(request):
    chapter_list = Chapter.objects.all()
    template = loader.get_template('helloAndroidUtil/chapters_index.html')
    context = {
        'chapters_list': chapter_list
    }
    return HttpResponse(template.render(context, request))
