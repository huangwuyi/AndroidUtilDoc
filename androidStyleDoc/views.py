from django.http import StreamingHttpResponse, FileResponse, HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import HuangwuyiStyle
import os


# Create your views here.
def hello(request):
    # my_response = response.HttpResponse()
    # my_response.content = "hello from androidStyleDoc"
    # return my_response
    styles = HuangwuyiStyle.objects.all()
    for style in styles:
        style.style_example_short = str(style.style_example)[(str(style.style_example)).rindex('/') + 1:]
        print(style.style_example.name)
        print(style.style_example.path)
    return render(request, "helloAndroidStyle.html", {"styles": styles})


def single_truck(request):
    dict_post = request.POST
    dict_cookies = request.COOKIES
    return render(request, "singleTruck.html", {"dict_post": dict_post, \
                                                "dict_cookies": dict_cookies})


def image_view(request, directory):
    my_dirt = dict()
    my_dirt["error"] = "yes"
    my_dirt["parameter"] = directory
    response = JsonResponse(my_dirt)
    return response
    # response = HttpResponse("directory:" + directory);
    # directory = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), directory)
    # if not os.path.isfile(directory):
    #     response = FileResponse(open(directory, 'r'), as_attachment=True)
    #     response.charset = 'UTF-8'
    # else:
    #     # response = HttpResponse()
    #     # response.write("not found" + directory)
    #     my_dirt = dict()
    #     my_dirt["errot"] = "yes"
    #     response = JsonResponse(my_dirt)
    # return response
