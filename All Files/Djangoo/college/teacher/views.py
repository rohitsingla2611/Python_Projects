# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher


def front_page(request):
    stds = Teacher
    return HttpResponse("</h1>Welcome Teachers</h1>")


def data(request):
    return HttpResponse("<table border =  2 cellspacing = 1 cellpadding = 10 bgcolor = 'cyan' bordercolor = 'red'>"
                        "<tr>"
                        "<th>ID</th>"
                        "<th>Name</th>"
                        "<th>Department</th>"
                        "</tr>"
                        "<tr>"
                        "<td>1.</td>"
                        "<td>Sehj</td>"
                        "<td>Python</td>"
                        "</tr>"
                        "<tr>"
                        "<td>2.</td>"
                        "<td>Sarang</td>"
                        "<td>Python</td>"
                        "</tr>"
                        "</table>")
