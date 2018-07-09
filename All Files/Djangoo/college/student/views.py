# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def front_page(request):
    stds = Student.objects.all()
    html = "<ol>"
    for std in stds:
        html += "<li>" + "<a href ='student/" + str(std.RollNo) + "'>" + str(std.Name) + "</a>" + "</li>"
    html += "</ol>"

    return HttpResponse(html)


def data(request, roll_no):
    return HttpResponse(
        roll_no + "<table border =  2 cellspacing = 1 cellpadding = 10 bgcolor = 'cyan' bordercolor = 'red'>"
                  "<tr>"
                  "<th>Roll No</th>"
                  "<th>Name</th>"
                  "<th>Class</th>"
                  "</tr>"
                  "<tr>"
                  "<td>1</td>"
                  "<td>Rohit Singla</td>"
                  "<td>BCA</td>"
                  "</tr>"
                  "<tr>"
                  "<td>2.</td>"
                  "<td>Harman</td>"
                  "<td>B.Tech</td>"
                  "</tr>"
                  "</table>"
                  "<br/>"
                  "</br>"
                  "<ol>"
                  "<li>Rohit</a></li>"
                  "<li>Dinesh</li>"
                  "<li>Pranav</li>"
                  "<li>Harman</li>"
                  "</ol>")
