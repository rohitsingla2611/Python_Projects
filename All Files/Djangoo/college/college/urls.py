"""college URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

import student
# from student import views
import teacher

# from teacher import views
from college import views

urlpatterns = [
    path('', views.front_page),
    path('admin/', admin.site.urls),
    path('teacher/', include("teacher.urls")),
    path('student/', include("student.urls")),

    # path('student/', student.views.front_page),
    # path('teacher/', teacher.views.front_page)

]
