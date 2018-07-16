from django.urls import path
from . import views
urlpatterns = [
    path("", views.hello_android_util),
    path("hello/", views.hello_android_util),
    path("chapter/", views.chapter),
    path("chapter/<int:chapter_lsno>/", views.chapter_item),
    path("chapter/<int:chapter_lsno>/<int:item_lsno>/", views.chapter_item_method),
    path("chapter2/", views.IndexView.as_view(), name='index'),
    path("chapter2/<int:pk>/", views.DetaiView.as_view(), name='detail'),
]



