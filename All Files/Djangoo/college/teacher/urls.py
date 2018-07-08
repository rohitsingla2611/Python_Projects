from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('Teacher_front/', views.front_page),
    path('Teacher_data/', views.front_page)
]
