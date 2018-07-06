from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello_android_util(requset):
    return render(requset, "HelloAndroidUtil.html")
    # return HttpResponse("Hello AndroidUtil")


def hello_android_util2(request):
    return HttpResponse("hello AndroidUtil2")

