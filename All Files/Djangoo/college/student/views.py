# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def front_page(request):
    return HttpResponse("</h1>Welcome Students</h1>")


def data(request):
    return HttpResponse("<table border =  2 cellspacing = 1 cellpadding = 10 bgcolor = 'cyan' bordercolor = 'red'>"
                        "<tr>"
                        "<th>Roll No</th>"
                        "<th>Name</th>"
                        "<th>Class</th>"
                        "</tr>"
                        "<tr>"
                        "<td>1.</td>"
                        "<td>Rohit Singla</td>"
                        "<td>BCA</td>"
                        "</tr>"
                        "<tr>"
                        "<td>2.</td>"
                        "<td>Harman</td>"
                        "<td>B.Tech</td>"
                        "</tr>"
                        "</table>")
