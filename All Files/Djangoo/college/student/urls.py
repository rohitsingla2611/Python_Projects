from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.front_page),
    re_path('(?P<roll_no>[0-9]{1})/', views.data),
    # re_path('data/', views.data)
]
