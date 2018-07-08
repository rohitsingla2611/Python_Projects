from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('Teacherfront/', views.front_page),
    path('Teacherdata/', views.data())
]
