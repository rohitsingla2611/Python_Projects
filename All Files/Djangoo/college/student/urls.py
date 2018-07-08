from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('Student_front/', views.front_page),
    path('student_data/', views.front_page)
]
