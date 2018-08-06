from . import views
from django.urls import path

urlpatterns = [
    path('', views.hello),
    path('single/', views.single_truck),
]
