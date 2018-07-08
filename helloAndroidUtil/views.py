from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
projectName = "AndroidUtil"


def hello_android_util(requset):
    return render(requset, "HelloAndroidUtil.html", {"projectName": projectName ,\
                                                     "timeSince":time.strftime("%y-%m-%d %H:%M:%S",time.gmtime())})

#
# def hello_android_util2(request):
#     return HttpResponse("hello AndroidUtil2")
