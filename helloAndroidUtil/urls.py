from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello_android_util),
    path("hello/", views.hello_android_util)
]
