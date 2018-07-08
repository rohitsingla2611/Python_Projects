from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_page),
    path('data/', views.data)
]
