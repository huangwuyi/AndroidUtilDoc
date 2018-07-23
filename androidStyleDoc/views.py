from django.http import response
from django.shortcuts import render
from .models import HuangwuyiStyle


# Create your views here.
def hello(request):
    # my_response = response.HttpResponse()
    # my_response.content = "hello from androidStyleDoc"
    # return my_response
    styles = HuangwuyiStyle.objects.all()
    for style in styles:
        style.style_example_short = str(style.style_example)[(str(style.style_example)).rindex('/')+1:]
    return render(request, "helloAndroidStyle.html", {"styles": styles})
