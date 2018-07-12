# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def front_page(request):
    return render(request, 'base1.html', {})
    # return HttpResponse("</h1>Welcome to Django</h1>"
    #                   "<br/>"
    #                  "</h1>Rohit Singla</h1>")
