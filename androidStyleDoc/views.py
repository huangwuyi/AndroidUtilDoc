from django.http import response
from django.shortcuts import render


# Create your views here.
def hello(request):
    # my_response = response.HttpResponse()
    # my_response.content = "hello from androidStyleDoc"
    # return my_response
    return render(request, "helloAndroidStyle.html")
