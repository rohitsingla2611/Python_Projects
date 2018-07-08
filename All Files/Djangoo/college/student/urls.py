from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('Student/front/', views.front_page),
    path('Student/data/', views.front_page)
]
