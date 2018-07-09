# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def front_page(request):
    return HttpResponse("</h1>Welcome Students</h1>")


def data(request):
    return HttpResponse("<table border =  2 cellspacing = 1 cellpadding = 10 bgcolor = 'cyan' bordercolor = 'red'>"
                        "<tr>"
                        "<th>Room No</th>"
                        "<th>Seats</th>"
                        "<th>Allotted to</th>"
                        "</tr>"
                        "<tr>"
                        "<td>1.</td>"
                        "<td>30</td>"
                        "<td>Computer Science</td>"
                        "</tr>"
                        "<tr>"
                        "<td>2.</td>"
                        "<td>50</td>"
                        "<td>Commerce</td>"
                        "</tr>"
                        "</table>")
