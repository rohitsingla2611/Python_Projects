# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def front_page(request):
    return HttpResponse("</h1>Welcome to Django</h1>"
                        "<\n>"
                        "</h1>Rohit Singla</h1>")
