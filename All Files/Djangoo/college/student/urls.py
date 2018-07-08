from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('front/', views.front_page),
    path('data/', views.data)
]
