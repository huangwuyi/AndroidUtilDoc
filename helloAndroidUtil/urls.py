from django.urls import path
from . import views
urlpatterns = [
    path("", views.hello_android_util),
    path("hello/", views.hello_android_util),
    path("chapter/",views.chapter),
    path("chapter/<int:chapter_lsno>/",views.chapter_item),
]

